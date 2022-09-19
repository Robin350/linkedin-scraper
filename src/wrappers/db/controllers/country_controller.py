from src.wrappers.db.controllers.base_controller import BaseController
from src.wrappers.db.entities.country import Country


class CountryController(BaseController):
    entity = Country
