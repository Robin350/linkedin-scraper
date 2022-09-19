import datetime
import logging
import json

from src.utils.exception import error_handling
from src.wrappers.linkedin.search import search_learning_companies

logger = logging.getLogger(__name__)


@error_handling
def main():
    start = datetime.datetime.now()
    companies = search_learning_companies("Python")
    with open("output.json", "w") as json_file:
        json_file.write(json.dumps(companies))

    end = datetime.datetime.now()
    logger.info(f"Done in {(end - start).total_seconds()}s.")


if __name__ == "__main__":
    main()
