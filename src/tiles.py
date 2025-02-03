from enum import Enum, auto

import glm

TILE_SIZE = 16


class Tile(Enum):
    BLACK = auto()
    DIRT = auto()
    TREES = auto()
    STAIRS = auto()
    LADDER = auto()
    ROCK_WALL = auto()
    WHITE_ROCK_WALL = auto()
    GREEN_BUSH = auto()
    BROWN_BUSH = auto()
    ROCK = auto()
    RAFT = auto()


COLLIDEABLE_TILES = set(
    (
        Tile.TREES,
        Tile.ROCK_WALL,
        Tile.WHITE_ROCK_WALL,
        Tile.GREEN_BUSH,
        Tile.BROWN_BUSH,
        Tile.ROCK,
    )
)


def is_tile_collidable(tile):
    if tile in COLLIDEABLE_TILES:
        return True
    return False


TILE_TEXTURE_SAMPLE_POSITIONS = {
    Tile.BLACK: glm.uvec2(1, 0),
    Tile.DIRT: glm.uvec2(2, 0),
    Tile.TREES: glm.uvec2(3, 0),
    Tile.STAIRS: glm.uvec2(0, 0),
    Tile.LADDER: glm.uvec2(4, 0),
    Tile.ROCK_WALL: glm.uvec2(0, 1),
    Tile.WHITE_ROCK_WALL: glm.uvec2(1, 1),
    Tile.GREEN_BUSH: glm.uvec2(2, 1),
    Tile.BROWN_BUSH: glm.uvec2(3, 1),
}


def get_tile_texture_sample_position(tile) -> glm.uvec2:
    return TILE_TEXTURE_SAMPLE_POSITIONS[tile]


def collidable_tile_in_list(tiles):
    for tile in tiles:
        collided = is_tile_collidable(tile)
        if collided:
            return True
    return False
