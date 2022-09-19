import logging

from src.config.tweepy import DEFAULT_MAX_TWEETS_PER_QUERY


logger = logging.getLogger(__name__)


def parse_tweepy_response(paginator):
    """
    Note: We need to manually iterate the pages, instead of using
    ".flatten(limit)" to be able to use the 'includes' field.
    this field carries information like the image true URL, or any
    extra fields we included.

    Explained by tweepy here:
    https://docs.tweepy.org/en/stable/faq.html#how-do-i-access-includes-data-while-using-paginator

    :return:
    """
    items_collected = 0
    response_list = []

    for page in paginator:
        if not page.data:
            break

        items_collected += 1
        if items_collected > DEFAULT_MAX_TWEETS_PER_QUERY:
            logger.info(f"Maximum tweepy items reached: {DEFAULT_MAX_TWEETS_PER_QUERY}")
            break
        if hasattr(page, "includes"):
            includes = _get_indexed_includes_dict(page.includes)
        else:
            includes = {}

        for item in page.data:
            item_dict = item
            _fill_includes_values(item_dict, includes)
            response_list.append(item_dict)
    return response_list


def _get_indexed_includes_dict(includes):
    includes_dict = {
        "media": {},
        "users": {},
        "poll": {},
        "place": {},
        "geo": {},
    }
    for include_type, values in includes.items():
        for value in values:
            if include_type == "media":
                id_ = value["media_key"]
            else:
                id_ = value["id"]
            includes_dict[include_type][id_] = value
    return includes_dict


def _fill_includes_values(item, includes):

    # media
    if item.attachments:
        media_ids = item.attachments["media_keys"]
        item.data["media"] = []
        for media_id in media_ids:
            item.data["media"].append(includes["media"][media_id])

    # users
    if item.author_id:
        user_id = item.author_id
        item.data["user"] = includes["users"][user_id]
