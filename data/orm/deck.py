import uuid

from sqlalchemy import ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from data.orm.base import Base
from models.color_set import ColorSet

class DeckORM(Base):
    __tablename__ = "decks"

    location_id: Mapped[uuid.UUID] = mapped_column(Uuid,
                                                   ForeignKey("locations.id"), 
                                                   nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    colors: Mapped[ColorSet] = mapped_column()