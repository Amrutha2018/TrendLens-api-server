from sqlalchemy.orm import Session
from app.models.youtube_filter import YouTubeFilter
from app.schemas.youtube_filter import YouTubeFilterCreate

def create_youtube_filter(db: Session, user_id: int, filter_data: YouTubeFilterCreate):
    db_filter = YouTubeFilter(
        user_id=user_id,
        title_keywords=filter_data.title_keywords,
        description_keywords=filter_data.description_keywords,
        comments_keywords=filter_data.comments_keywords,
        exact_phrases=filter_data.exact_phrases,
        channel_name=filter_data.channel_name,
        channel_subscriber_min=filter_data.channel_subscriber_min,
        channel_subscriber_max=filter_data.channel_subscriber_max,
        minimum_views=filter_data.minimum_views,
        minimum_likes=filter_data.minimum_likes,
        minimum_comments=filter_data.minimum_comments,
        minimum_comment_likes=filter_data.minimum_comment_likes,
        upload_start_date=filter_data.upload_start_date,
        upload_end_date=filter_data.upload_end_date,
        comment_start_date=filter_data.comment_start_date,
        comment_end_date=filter_data.comment_end_date,
        video_type=filter_data.video_type,
        duration_min=filter_data.duration_min,
        duration_max=filter_data.duration_max,
    )
    db.add(db_filter)
    db.commit()
    db.refresh(db_filter)
    return db_filter
