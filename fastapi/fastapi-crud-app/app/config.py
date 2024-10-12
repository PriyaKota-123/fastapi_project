from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
