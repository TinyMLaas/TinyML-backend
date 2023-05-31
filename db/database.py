from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.environ.get("DATABASE_URL")

def session(DATABASE_URL=DATABASE_URL):
    # "check_same_thread": False needed only for sqlite
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )

    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )

    return SessionLocal()

Base = declarative_base()
