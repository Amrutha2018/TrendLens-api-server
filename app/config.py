import os
from dotenv import load_dotenv

load_dotenv()


app_config = {
    "secret_key": os.getenv("SECRET_KEY")
}

postgres_config = {
    "postgres_url" : os.getenv("DATABASE_URL")
}