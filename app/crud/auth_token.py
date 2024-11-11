from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from app.models.auth_token import AuthToken
import uuid

def create_auth_token(db: Session, user_id: int, expiration_minutes: int = 15):
    token = str(uuid.uuid4())
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=expiration_minutes)
    db_token = AuthToken(user_id=user_id, token=token, expires_at=expires_at)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token