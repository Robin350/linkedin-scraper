from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.wrappers.db.connect import BaseClass


class Association(BaseClass):
    __tablename__ = "association"
        
    id = Column(Integer, primary_key=True)
    countrypathology_id = Column(Integer, ForeignKey("countrypathology.id"))
    association_type_id = Column(Integer, ForeignKey("association_type.id"))
    name = Column(String(256))
    twitter = Column(String(128))
    linkedin = Column(String(256))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    countrypathology = relationship("CountryPathology", back_populates="associations")
