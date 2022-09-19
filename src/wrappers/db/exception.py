import logging

from src.utils.exception import GenericException, error_handling

logger = logging.getLogger(__name__)


class DBException(GenericException):

    @classmethod
    @error_handling
    def error_handling(cls, function):
        def wrapper(*args, **kwargs):
            try:
                response = function(*args, **kwargs)
                return response
            except GenericException as e:
                raise e
            except Exception as e:
                msg = f"'{function.__name__}' - Unexpected error in DB: '{e}'"
                logger.error(msg)
                raise DBException(msg)

        wrapper.__name__ = function.__name__
        return wrapper
