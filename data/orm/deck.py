import uuid

from sqlalchemy import ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.base import Base
from data.orm.types import ColorSetType
from models.color_set import ColorSet


class DeckORM(Base):
    """
    TODO: Maybe format should be its own model? That seems like it might 
    encapsulate rules and card legality better.
    I only play commmander and eternal/casual though, so meh.
    """
    __tablename__ = "decks"

    location_id: Mapped[uuid.UUID] = mapped_column(Uuid,
                                                   ForeignKey("locations.id"), 
                                                   nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    colors: Mapped[ColorSet] = mapped_column(ColorSetType, nullable=True)
    format: Mapped[str] = mapped_column(String)

    location: Mapped["LocationORM"] = relationship(back_populates="decks")
    card: Mapped["CardORM"] = relationship(back_populates="deck")
