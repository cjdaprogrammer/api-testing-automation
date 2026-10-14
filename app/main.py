from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


app = FastAPI(
    title="Task Management API",
    description="A portfolio project for REST API testing automation.",
    version="1.0.0",
)


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)
    completed: bool = False


class Task(TaskCreate):
    id: int


tasks: dict[int, Task] = {}
next_task_id = 1


@app.get("/")
def root():
    return {
        "message": "Task Management API is running",
        "docs": "/docs",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    global next_task_id

    task = Task(id=next_task_id, **task_data.model_dump())
    tasks[next_task_id] = task
    next_task_id += 1

    return task


@app.get("/tasks")
def get_tasks():
    return list(tasks.values())


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = tasks.get(task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_data: TaskCreate):
    if task_id not in tasks:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    updated_task = Task(id=task_id, **task_data.model_dump())
    tasks[task_id] = updated_task

    return updated_task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    del tasks[task_id]

    return {"message": "Task deleted successfully"}