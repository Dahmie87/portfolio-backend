from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


import os
from dotenv import load_dotenv  # type: ignore

load_dotenv()
DB_URL = os.getenv("DATABASE_URL")
if not DB_URL:
    DB_URL = "sqlite:///./app.db"

engine = create_engine(DB_URL, connect_args={
    "check_same_thread": False})

session = sessionmaker(bind=engine)

Base = declarative_base()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
