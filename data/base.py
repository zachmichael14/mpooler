from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DATABASE_PATH = Path("data/collection.db")


def get_engine():
    db_url = f"sqlite:///{DATABASE_PATH}"
    return create_engine(db_url)

engine = get_engine()
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass
