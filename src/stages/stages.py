from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import List

from src.tiles import Tile

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.entity import Entity

"""
    there will be a screen for each 16x11 room from zelda 1
    each screen will have a string of tiles and a list of entities
"""


class StageType(Enum):
    START = auto()


@dataclass(frozen=True)
class StageDef:
    tiles_string: str
    entities: List[Entity]
    left: StageType
    right: StageType
    up: StageType
    down: StageType


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

SCREEN_START = StageDef(
    """
rrrrrrrrrrrrrrrr
rddddddddddddddr
rddddddddddddddr
rddddddddddddddr
rddddddddddddddr
dddddddddddddddd
dddddddddddddddd
rddddddddddddddr
rddddddddddddddr
rddddddddddddddr
rrrrrrrrrrrrrrrr
""",
    [],
    StageType.START,
    StageType.START,
    StageType.START,
    StageType.START,
)

STAGES = {
    StageType.START: SCREEN_START,
}
