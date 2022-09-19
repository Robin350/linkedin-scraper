from src.wrappers.db.controllers.base_controller import BaseController
from src.wrappers.db.entities.twitter import Twitter


class TwitterController(BaseController):
    entity = Twitter
