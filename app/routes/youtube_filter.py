from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.youtube_filter import YouTubeFilterCreate
from app.crud.youtube_filter import create_youtube_filter
from app.database import get_db
from app.utils.auth import get_current_user_id

router = APIRouter()

@router.post("/youtube")
def create_youtube_filter_endpoint(
    filter_data: YouTubeFilterCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    return create_youtube_filter(db=db, user_id=user_id, filter_data=filter_data)
