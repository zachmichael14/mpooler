from dataclasses import dataclass, field
from decimal import Decimal
from uuid import UUID

from models.color_set import ColorSet

@dataclass
class Card:
    """
    This is a combination of select fields from the Scryfall API
    and internal fields.

    TODO:     there's not currently a way to specify if a card is 
    borderless/foil/full-art, etc. Also, I'm not really sure what 
    fields will be useful here, but I'm not trying to store all 
    scryfall info.
    """
    collection_id: UUID
    location_id: UUID
    scryfall_id: UUID
    gatherer_resource_id: str = ""
    tcgplayer_product_id: int = 0
    name: str
    color_identity: ColorSet = field(default_factory=ColorSet)
    color: ColorSet = field(default_factory=ColorSet)
    cmc: Decimal = Decimal("0")
    mana_cost: str = "" # Can contain "X" and such
    type_line: str = ""
    set_name: str = ""
    set_code: str = ""
    set_id: UUID | None = None
    rarity: str = ""
    printed_text: str = ""
    oracle_text: str = ""
    keywords: list[str] = field(default_factory=list)
    flavor_text: str = ""
    power: str = ""
    toughness: str = ""
    collector_number: str = "" # Can contain letters or *
    artists: list[str] = field(default_factory=list)
    condition: str = "MP"
    internally_reserved: bool = False
    prints_search_uri: str = ""
    scryfall_uri: str = ""
