from dataclasses import dataclass, field
from uuid import UUID

from models.color_set import ColorSet

# TODO: Maybe format should be its own model? That seems like it might 
# encapsulate rules and legality better.
# I only play commmander and eternal/casual, so it's not necessary for now
@dataclass
class Deck:
    deck_id: UUID
    name: str
    format: str
    colors: ColorSet = field(default_factory=ColorSet)
