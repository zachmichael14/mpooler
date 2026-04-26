import uuid

from sqlalchemy import ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.orm.base import Base
from data.orm.types import ColorSetType
from models.color_set import ColorSet


class DeckORM(Base):
    __tablename__ = "decks"

    location_id: Mapped[uuid.UUID] = mapped_column(Uuid,
                                                   ForeignKey("locations.id"), 
                                                   nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    colors: Mapped[ColorSet] = mapped_column(ColorSetType, nullable=True)
    format: Mapped[str] = mapped_column(String)

    location: Mapped["LocationORM"] = relationship(back_populates="decks")
    card: Mapped["CardORM"] = relationship(back_populates="deck")
