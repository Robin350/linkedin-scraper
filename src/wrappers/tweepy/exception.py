import logging

from tweepy.errors import \
    TweepyException, \
    HTTPException, \
    BadRequest, \
    Unauthorized, \
    Forbidden, \
    NotFound, \
    TooManyRequests

from src.utils.exception import GenericException, error_handling

logger = logging.getLogger(__name__)


class TweepyWrapperException(GenericException):

    @classmethod
    @error_handling
    def error_handling(cls, function):
        def wrapper(*args, **kwargs):
            try:
                response = function(*args, **kwargs)
                return response
            except GenericException as e:
                raise e
            except TooManyRequests as e:
                msg = f"'{function.__name__}' - Twitter API - Too many requests: '{e}'"
                logger.error(msg)
                raise TweepyWrapperException(msg)
            except NotFound as e:
                msg = f"'{function.__name__}' - Twitter API - Entity not found: '{e}'"
                logger.error(msg)
                raise TweepyWrapperException(msg)
            except Forbidden as e:
                msg = f"'{function.__name__}' - Twitter API - Forbidden access: '{e}'"
                logger.error(msg)
                raise TweepyWrapperException(msg)
            except Unauthorized as e:
                msg = f"'{function.__name__}' - Twitter API - Request is not authorized: '{e}'"
                logger.error(msg)
                raise TweepyWrapperException(msg)
            except BadRequest as e:
                msg = f"'{function.__name__}' - Twitter API - Invalid request parameters: '{e}'"
                logger.error(msg)
                raise TweepyWrapperException(msg)
            except HTTPException as e:
                msg = f"'{function.__name__}' - Twitter API - Unexpected error: '{e}'"
                logger.error(msg)
                raise TweepyWrapperException(msg)
            except TweepyException as e:
                msg = f"'{function.__name__}' - Tweepy - Unexpected error: '{e}'"
                logger.error(msg)
                raise TweepyWrapperException(msg)
            except Exception as e:
                msg = f"'{function.__name__}' - Unexpected error in code: '{e}'"
                logger.error(msg)
                raise TweepyWrapperException(msg)

        wrapper.__name__ = function.__name__
        return wrapper
