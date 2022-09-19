import logging

from src.wrappers.tweepy.exception import TweepyWrapperException
from src.wrappers.tweepy.connect import tweepy_connection
from src.wrappers.tweepy.query_builder import build_paginator_query
from src.wrappers.tweepy.response_parser import parse_tweepy_response

logger = logging.getLogger(__name__)


@TweepyWrapperException.error_handling
def search_tweets(query):

    parameters = {"query": query}
    paginator = build_paginator_query(tweepy_connection.api_client.get_users_tweets, parameters)
    response = parse_tweepy_response(paginator)

    return response
