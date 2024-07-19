import dotenv
import os

dotenv.load_dotenv()

DATABASE_USER = os.getenv("DATABASE_USER")
NAME_DATABASE = os.getenv("NAME_DATABASE")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
HOST = os.getenv("HOST")
DATABASE_LOG_SETTINGS = os.getenv("DATABASE_LOG_SETTINGS")
DEVELOPER_EMAIL = os.getenv("DEVELOPER_EMAIL")