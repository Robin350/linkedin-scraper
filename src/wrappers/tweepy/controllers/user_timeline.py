import logging

from src.wrappers.tweepy.exception import TweepyWrapperException
from src.wrappers.tweepy.connect import tweepy_connection
from src.wrappers.tweepy.query_builder import build_paginator_query
from src.wrappers.tweepy.response_parser import parse_tweepy_response

logger = logging.getLogger(__name__)


@TweepyWrapperException.error_handling
def get_user_timeline(username, start_date=None, end_date=None):
    user_handle = username.replace("@", "")
    user = tweepy_connection.api_client.get_user(username=user_handle)

    parameters = {"id": user.data["id"], "exclude": "retweets,replies"}
    if start_date:
        parameters["start_date"] = start_date
    if end_date:
        parameters["end_date"] = end_date

    paginator = build_paginator_query(tweepy_connection.api_client.get_users_tweets, parameters)
    response = parse_tweepy_response(paginator)

    return response
