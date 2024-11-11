from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.hashing import hash_password

def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, password_hash=hash_password(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    """Retrieve a user by their email address."""
    return db.query(User).filter(User.email == email).first()
