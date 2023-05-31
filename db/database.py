import os
from dotenv import load_dotenv

load_dotenv()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#DATABASE_URL = os.getenv("DATABASE_URL")

# this needs to be a function so we can start a test instance
def session(DATABASE_URL=os.getenv("DATABASE_URL")):
    # "check_same_thread": False needed only for sqlite
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )

    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )

    return SessionLocal

Base = declarative_base()
