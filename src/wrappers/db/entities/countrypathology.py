from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.wrappers.db.connect import BaseClass


class CountryPathology(BaseClass):
    __tablename__ = "countrypathology"
        
    id = Column(Integer, primary_key=True)
    pathology_id = Column(Integer, ForeignKey("pathology.id"))
    country_id = Column(Integer, ForeignKey("country.id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    pathology = relationship("Pathology")
    keyword_pathologies = relationship("KeywordPathology")
    competitors = relationship("Competitor", back_populates="countrypathology")
    associations = relationship("Association", back_populates="countrypathology")
    tweets = relationship("Twitter")
