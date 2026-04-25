from dataclasses import dataclass
from enum import Enum
from uuid import UUID


class LocationType(Enum):
    DECK = "DECK"
    BINDER = "BINDER"
    BOX = "BOX"
    BULK = "BULK"
    OTHER = "OTHER"


@dataclass
class Location:
    """
    The name and type of the physical location of a card.

    It's basically a way to specify the location of cards that aren't in decks."""
    location_id: UUID
    name: str
    location_type: LocationType
