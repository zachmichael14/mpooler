from enum import Enum

class Condition(Enum):
    """
    TODO: It might be beneficial to define __lt__, __gt__ methods
    so comparison can be made (ex., find all near mint/damaged cards, etc.)
    """
    NM  = "NM"   # Near Mint
    LP  = "LP"   # Lightly Played
    MP  = "MP"   # Moderately Played
    HP  = "HP"   # Heavily Played
    DMG = "DMG"  # Damaged