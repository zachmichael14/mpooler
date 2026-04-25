from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.orm.base import Base

class LocationORM(Base):
    """
    The physical location of a card.
    """
    __tablename__ = "locations"

    name: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False) # LocationType

    # String keeps theses lists forward-references for typing
    cards: Mapped[list["CardORM"]] = relationship(back_populates="location")
    decks: Mapped[list["DeckORM"]] = relationship(back_populates="location")
