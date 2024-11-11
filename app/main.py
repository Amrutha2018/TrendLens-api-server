from fastapi import FastAPI

from app.routes.api_router import api_router
from app.database import Base, engine

app = FastAPI()

app.include_router(api_router)