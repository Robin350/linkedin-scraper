import logging
import tweepy


logger = logging.getLogger(__name__)

DEFAULT_PARAMETERS = {
    "expansions": "attachments.media_keys,author_id",
    "tweet_fields": "entities,created_at",
    "media_fields": "media_key,url",
    "user_fields": "username"
}


def build_paginator_query(method, args_json):
    query_parameters = DEFAULT_PARAMETERS.copy()
    query_parameters.update(args_json)

    paginator = tweepy.Paginator(method, **query_parameters)

    return paginator
