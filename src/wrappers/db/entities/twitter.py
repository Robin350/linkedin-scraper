from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date

from src.wrappers.db.connect import BaseClass


class Twitter(BaseClass):
    __tablename__ = "twitter"
        
    id = Column(Integer, primary_key=True)
    tweet_id = Column(String(128))
    content = Column(String(8192))
    url = Column(String(512))
    image = Column(String)
    image_ocr = Column(String)
    account = Column(String(128))
    user_name = Column(String(128))
    post_date = Column(Date)
    drugs_ids = Column(String(128))
    competitor_id = Column(Integer, ForeignKey("competitor.id"))
    association_type_id = Column(Integer, ForeignKey("association_type.id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    countrypathology_id = Column(Integer, ForeignKey("countrypathology.id"))
