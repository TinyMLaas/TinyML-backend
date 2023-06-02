import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


def session():
    """Sets up the database connection.

    Args:
        DATABASE_URL (str, optional): Defaults to DATABASE_URL from environment variables.

    Returns:
        sessionmaker: Local database session.
    """

    DATABASE_URL = os.environ.get("DATABASE_URL")

    # "check_same_thread": False needed only for sqlite
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )

    session_local = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )

    return session_local()


def get_db():
    """Sets up the database session.

    Yields:
        session(): Database session.
    """
    database = session()
    try:
        yield database
    finally:
        database.close()

Base = declarative_base()
