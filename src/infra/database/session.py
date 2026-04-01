from src.domain.entities.user_model import Users
from src.domain.entities.category_model import Categories
from sqlmodel import create_engine, SQLModel
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(os.getenv("DB_URL", ""))

def create_tables():
    SQLModel.metadata.create_all(engine)