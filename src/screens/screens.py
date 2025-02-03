from dataclasses import dataclass
from enum import Enum, auto
from typing import List

from src.entity import Entity
from src.tiles import Tile

"""
    there will be a screen for each 16x11 room from zelda 1
    each screen will have a string of tiles and a list of entities
"""


class Screens(Enum):
    START = auto()


@dataclass(frozen=True)
class Screen:
    tiles_string: str
    entities: List[Entity]
    left: Screens
    right: Screens
    up: Screens
    down: Screens


LETTER_TO_TILE_KEY = {
    "b": Tile.BLACK,
    "d": Tile.DIRT,
    "t": Tile.TREES,
    "s": Tile.STAIRS,
    "l": Tile.LADDER,
    "r": Tile.ROCK_WALL,
    "w": Tile.WHITE_ROCK_WALL,
    "g": Tile.GREEN_BUSH,
    "n": Tile.BROWN_BUSH,
    "o": Tile.ROCK,
    "f": Tile.RAFT,
}

SCREEN_START = Screen(
    """
rrrrrrrrrrrrrrrr
rddddddddddddddr
rddddddddddddddr
rddddddddddddddr
rddddddddddddddr
rddddddddddddddr
dddddddddddddddd
rddddddddddddddr
rddddddddddddddr
rddddddddddddddr
rddddddddddddddr
rrrrrrrrrrrrrrrr
""",
    [],
    Screens.START,
    Screens.START,
    Screens.START,
    Screens.START,
)

SCREENS = {
    Screens.START: SCREEN_START,
}
