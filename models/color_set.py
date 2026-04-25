from dataclasses import dataclass, field
from enum import Enum


class ManaColor(Enum):
    W = "W"
    U = "U"
    B = "B"
    R = "R"
    G = "G"


@dataclass
class ColorSet:
    """TODO: How to handle colorless? It's not a color, so adding it here seems inappropriate. Maybe just a lack of colors (length == 0) is adequate"""
    # default_factory creates an empty set of ManaColors upon instantiation
    colors: set[ManaColor] = field(default_factory=set)

    def to_string_list(self) -> list[str]:
        """Return the ColorSet as a list of color letters."""
        return [color.value for color in self.colors]
    
    @classmethod
    def from_string_list(cls, values: list[str]) -> "ColorSet":
        """Create a ColorSet from a list of color letters."""
        return cls(colors={ManaColor(value) for value in values})
