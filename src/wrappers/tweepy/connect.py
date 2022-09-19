import logging
import tweepy

from src.config.tweepy import \
    ACCESS_TOKEN, \
    ACCESS_SECRET, \
    CONSUMER_SECRET, \
    CONSUMER_KEY, \
    BEARER_TOKEN

from src.wrappers.tweepy.exception import TweepyWrapperException, TweepyException

logger = logging.getLogger(__name__)


class TweepyConnection:

    def __init__(self, wait_on_rate_limit=True):
        self.api_client = None
        self._auth_type = None
        self.__wait_on_rate_limit = wait_on_rate_limit
        self.__initialize_client()

    @TweepyWrapperException.error_handling
    def __initialize_client(self):
        """
        Initializes Twitter API client using Tweepy.
        Tries to set auth using bearer token, if it is not set or fails,
        uses [consumer_secret, consumer_key, access_token, access_token_secret] instead
        """
        bearer_token = BEARER_TOKEN
        access_token = ACCESS_TOKEN
        access_token_secret = ACCESS_SECRET
        consumer_key = CONSUMER_KEY
        consumer_secret = CONSUMER_SECRET

        if bearer_token:
            try:
                self.__initialize_client_with_bearer_token_auth(bearer_token)
            except TweepyException as e:
                logger.warning(
                    f"Tweepy authentication using bearer token failed, "
                    f"fallback to consumer key/secret auth. Error: {e}"
                )
                self.__initialize_client_with_consumer_keys_auth(
                    consumer_key,
                    consumer_secret,
                    access_token,
                    access_token_secret
                )
        else:
            self.__initialize_client_with_consumer_keys_auth(
                consumer_key,
                consumer_secret,
                access_token,
                access_token_secret
            )

    def __initialize_client_with_bearer_token_auth(self, bearer_token):
        self.api_client = tweepy.Client(bearer_token, wait_on_rate_limit=self.__wait_on_rate_limit)
        self._auth_type = "bearer_token"

    def __initialize_client_with_consumer_keys_auth(
            self,
            consumer_key,
            consumer_secret,
            access_token,
            access_token_secret
    ):
        self.api_client = tweepy.Client(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
            wait_on_rate_limit=self.__wait_on_rate_limit
        )
        self._auth_type = "consumer_key"


tweepy_connection = TweepyConnection()
