from sqlalchemy import Column, Integer, String, DateTime

from src.wrappers.db.connect import BaseClass


class Pathology(BaseClass):
    __tablename__ = "pathology"

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
