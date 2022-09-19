import logging

from src.wrappers.db.connect import db_connection


class BaseController:
    logger = logging.getLogger(__name__)
    entity = None

    @classmethod
    def get(cls, identifier, session=None):
        cls.logger.debug(f"Getting {identifier} from {cls.entity.__class__}")
        if session:
            return session.query(cls.entity).get(identifier)
        with db_connection.session_scope() as session:
            return session.query(cls.entity).get(identifier)

    @classmethod
    def list(cls, session=None):
        cls.logger.debug(f"Listing all objects from {cls.entity.__class__}")
        if session:
            return session.query(cls.entity).all()
        with db_connection.session_scope() as session:
            return session.query(cls.entity).all()

    @classmethod
    def filter(cls, filters, session=None):
        cls.logger.debug(f"Filtering '{filters}' from {cls.entity.__class__}")
        if session:
            return session.query(cls.entity).filter(filters).all()
        with db_connection.session_scope() as session:
            return session.query(cls.entity).filter(filters).all()

    @classmethod
    def add(cls, entity, session=None):
        cls.logger.debug(f"Adding new entity '{entity}' to {cls.entity.__class__}")
        if session:
            session.add(entity)
        with db_connection.session_scope() as session:
            session.add(entity)
