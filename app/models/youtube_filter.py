from sqlalchemy import Column, Integer, String, Date, ForeignKey, TIMESTAMP, ARRAY
from sqlalchemy.sql import func
from app.database import Base

class YouTubeFilter(Base):
    __tablename__ = "youtube_filters"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title_keywords = Column(ARRAY(String), nullable=True)
    description_keywords = Column(ARRAY(String), nullable=True)
    comments_keywords = Column(ARRAY(String), nullable=True)
    exact_phrases = Column(ARRAY(String), nullable=True)
    channel_name = Column(ARRAY(String), nullable=True)
    channel_subscriber_min = Column(Integer, nullable=True)
    channel_subscriber_max = Column(Integer, nullable=True)
    minimum_views = Column(Integer, nullable=True)
    minimum_likes = Column(Integer, nullable=True)
    minimum_comments = Column(Integer, nullable=True)
    minimum_comment_likes = Column(Integer, nullable=True)
    upload_start_date = Column(Date, nullable=True)
    upload_end_date = Column(Date, nullable=True)
    comment_start_date = Column(Date, nullable=True)
    comment_end_date = Column(Date, nullable=True)
    video_type = Column(String, nullable=True)
    duration_min = Column(Integer, nullable=True)
    duration_max = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
