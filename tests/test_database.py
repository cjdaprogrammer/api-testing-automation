from unittest.mock import MagicMock, patch

from app.database import get_db


def test_get_db_yields_session_and_closes_it():
    mock_session = MagicMock()

    with patch("app.database.SessionLocal", return_value=mock_session):
        db_generator = get_db()

        yielded_session = next(db_generator)

        assert yielded_session is mock_session

        try:
            next(db_generator)
        except StopIteration:
            pass

        mock_session.close.assert_called_once()


def test_get_db_closes_session_when_generator_throws_error():
    mock_session = MagicMock()

    with patch("app.database.SessionLocal", return_value=mock_session):
        db_generator = get_db()

        yielded_session = next(db_generator)
        assert yielded_session is mock_session

        try:
            db_generator.throw(RuntimeError("Simulated database error"))
        except RuntimeError as error:
            assert str(error) == "Simulated database error"

        mock_session.close.assert_called_once()