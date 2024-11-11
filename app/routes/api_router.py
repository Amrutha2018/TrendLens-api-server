from fastapi import APIRouter
from app.routes import auth, youtube_filter  

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth")
api_router.include_router(youtube_filter.router, prefix="/filter")