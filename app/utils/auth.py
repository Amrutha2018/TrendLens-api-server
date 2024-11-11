from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from app.database import get_db
from app.models.auth_token import AuthToken


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_user_id(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> int:
    db_token = db.query(AuthToken).filter(AuthToken.token == token).first()

    if db_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    print(db_token.expires_at)
    print(datetime.now(timezone.utc))
    if db_token.expires_at < datetime.now(timezone.utc):
        db.delete(db_token)
        db.commit()
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return db_token.user_id
