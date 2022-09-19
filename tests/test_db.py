from src.wrappers.db.connect import db_connection


def test_db_connection():
    with db_connection.session_scope() as _:
        pass
