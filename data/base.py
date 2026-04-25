from pathlib import Path
import uuid

from sqlalchemy import create_engine, Uuid
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column


DATABASE_PATH = Path("data/collection.db")


def get_engine():
    db_url = f"sqlite:///{DATABASE_PATH}"
    return create_engine(db_url)

engine = get_engine()
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    id: Mapped[uuid.UUID] = mapped_column(Uuid,
                                          primary_key=True,
                                          default=uuid.uuid4)
