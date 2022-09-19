import logging
import json
import os

logger = logging.getLogger(__name__)


def load_env_var(key, default=None):
    """
    Returns the value of the environment variable or None if not found.

    :param key: Environment variable key
    :param default: Default value to return if env var is not set
    :return: The environment variable value, or None
    """
    value = os.environ.get(key, default=default)

    if value is None:
        logger.warning(f"Environment variable '{key}' not found.")
    return value


def load_json_file(json_file_path):
    """
    Loads a JSON file content into a dict object.
    :param json_file_path: path to the JSON file
    :return: The dict object with the JSON content
    """

    with open(json_file_path, "r") as json_file:
        content = json.load(json_file)

    return content
