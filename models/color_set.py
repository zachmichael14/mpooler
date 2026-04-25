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
