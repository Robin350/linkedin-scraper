from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.orm import relationship

from src.wrappers.db.connect import BaseClass


class Country(BaseClass):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    code = Column(String(8))
    show_therapeutic_areas = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    countrypathologies = relationship("CountryPathology")
