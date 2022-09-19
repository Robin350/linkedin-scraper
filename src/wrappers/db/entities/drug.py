from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from src.wrappers.db.connect import BaseClass


class Drug(BaseClass):
    __tablename__ = "drug"
        
    id = Column(Integer, primary_key=True)
    competitor_id = Column(Integer, ForeignKey("competitor.id"))
    name = Column(String(256))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
