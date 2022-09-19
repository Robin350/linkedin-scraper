from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.wrappers.db.connect import BaseClass


class Competitor(BaseClass):
    __tablename__ = "competitor"

    id = Column(Integer, primary_key=True)
    countrypathology_id = Column(Integer, ForeignKey("countrypathology.id"))
    name = Column(String(256))
    logo = Column(String(256))
    color = Column(String(9))
    websites = Column(String(1024))
    areas = Column(String(512))
    twitter = Column(String(128))
    linkedin = Column(String(256))
    main = Column(Integer)
    visible = Column(Integer)
    parent_id = Column(Integer, ForeignKey("competitor.id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    tweets = relationship("Twitter")
    countrypathology = relationship("CountryPathology", back_populates="competitors")
    drugs = relationship("Drug")
