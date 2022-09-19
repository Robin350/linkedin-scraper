import logging

from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import MetaData, create_engine
from contextlib import contextmanager

from src.config.rds import SQL, USERNAME, PASSWORD, HOST, PORT, DATABASE
from src.wrappers.db.exception import DBException

logger = logging.getLogger(__name__)
BaseClass = declarative_base()


class DBConnection:

    @DBException.error_handling
    def __init__(self,
                 sql=SQL,
                 username=USERNAME,
                 password=PASSWORD,
                 host=HOST,
                 port=PORT,
                 database=DATABASE
                 ):
        """
        Initializes a SQL engine connected to the DB
        and a SQLAlchemy Session Maker using this engine.
        """
        self.url = f"{sql}://{username}:{password}@{host}:{port}/{database}"

        self.__engine = self.__create_db_engine()
        self.__session_maker = self.__initialize_session_maker()
        self.metadata = self.__retrieve_db_metadata()

    @DBException.error_handling
    def __create_db_engine(self):
        """
        Creates a DB engine connected to the url set in the attributes.

        :return: The DB engine
        """
        url = self.url

        try:
            engine = create_engine(url, echo=False)
            return engine
        except Exception as e:
            logger.error(f"Unexpected error creating DB engine: '{e}'")
            raise e

    @DBException.error_handling
    def __initialize_session_maker(self):
        """
        Initializes a SQLAlchemy Session Maker using the engine stored in the attributes.

        :return: The Session Maker
        """
        engine = self.__engine

        session_maker = sessionmaker()
        session_maker.configure(bind=engine)
        return session_maker

    @DBException.error_handling
    def __retrieve_db_metadata(self):
        """
        Retrieves all the DB MetaData from the engine set in the attributes.

        :return: The DB metadata
        """
        engine = self.__engine

        metadata = MetaData(bind=engine)
        metadata.reflect()
        return metadata

    @contextmanager
    def session_scope(self):
        """
        Provide a transactional scope around a series of operations.
        When the session ends, either commits or rollback depending
        on the result, and always ensures the session is closed.

        """
        session = self.__session_maker(expire_on_commit=False)
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()


db_connection = DBConnection()
