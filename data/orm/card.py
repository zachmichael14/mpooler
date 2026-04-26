import uuid

from sqlalchemy import (
    Boolean,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    Uuid
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.base import Base
from data.orm.types import ColorSetType, ConditionType
from models.condition import Condition
from models.color_set import ColorSet

class CardORM(Base):
    """
    This is a combination of select fields from the Scryfall API
    and internal fields.

    TODO:     there's not currently a way to specify if a card is 
    borderless/foil/full-art, etc. Also, I'm not really sure what 
    fields will be useful here, but I'm not trying to store all 
    scryfall info.
    """
    __tablename__ = "cards"

    location_id: Mapped[uuid.UUID] = mapped_column(Uuid,
                                                   ForeignKey("locations.id"),
                                                   nullable=False)
    deck_id: Mapped[uuid.UUID] = mapped_column(Uuid,
                                               ForeignKey("decks.id"),
                                               nullable=True)
    scryfall_id: Mapped[uuid.UUID] = mapped_column(Uuid,
                                                   nullable=True)  
    gatherer_id: Mapped[str | None] = mapped_column(String,
                                                    nullable=True)
    tcgplayer_id: Mapped[int | None] = mapped_column(Integer,
                                                     nullable=True)
    name: Mapped[str] = mapped_column(String,
                                      nullable=False)
    mana_cost: Mapped[str | None] = mapped_column(String)
    cmc: Mapped[float | None] = mapped_column(Numeric)
    color: Mapped[ColorSet | None] = mapped_column(ColorSetType)
    color_identity: Mapped[ColorSet | None] = mapped_column(ColorSetType)
    type_line: Mapped[str | None] = mapped_column(String)
    oracle_text: Mapped[str | None] = mapped_column(Text)
    power: Mapped[str | None] = mapped_column(String)
    toughness: Mapped[str | None] = mapped_column(String)
    rarity: Mapped[str | None] = mapped_column(String)
    set_name: Mapped[str | None] = mapped_column(String)
    set_code: Mapped[str | None] = mapped_column(String)
    set_id: Mapped[uuid.UUID | None] = mapped_column(Uuid,
                                                     nullable=True)
    collector_number: Mapped[str | None] = mapped_column(String)
    flavor_text: Mapped[str | None] = mapped_column(Text)
    condition: Mapped[Condition] = mapped_column(ConditionType,
                                                 default=Condition.MP,
                                                 nullable=False)
    foil: Mapped[bool] = mapped_column(Boolean,
                                       default=False)
    prints_search_uri: Mapped[str | None] = mapped_column(String)
    scryfall_uri: Mapped[str | None] = mapped_column(String)
    keywords: Mapped[str | None] = mapped_column(Text)
    artists: Mapped[str | None] = mapped_column(Text)
    is_reserved: Mapped[bool] = mapped_column(Boolean,
                                              default=False)

    location: Mapped["LocationORM"] = relationship(back_populates="cards")
    deck: Mapped["DeckORM | None"] = relationship(back_populates="cards")