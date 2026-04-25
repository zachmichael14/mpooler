from dataclasses import dataclass, field
from enum import Enum


class ManaColor(Enum):
    W = "W"
    U = "U"
    B = "B"
    R = "R"
    G = "G"


@dataclass
class Color:
    # default_factory creates an empty set of ManaColors upon instantiation
    colors: set[ManaColor] = field(default_factory=set)
