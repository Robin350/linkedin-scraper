from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from src.wrappers.db.connect import BaseClass


class KeywordPathology(BaseClass):
    __tablename__ = "keyword_pathology"
        
    id = Column(Integer, primary_key=True)
    countrypathology_id = Column(Integer, ForeignKey("countrypathology.id"))
    keyword = Column(String(256))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
