from enum import Enum, auto

import glm

TILE_SIZE = 16


class Tile(Enum):
    BLACK = auto()
    DIRT = auto()
    TREES = auto()
    TREES_TR = auto()
    TREES_TL = auto()
    TREES_BR = auto()
    TREES_BL = auto()


COLLIDEABLE_TILES = set(
    (
        Tile.DIRT,
        Tile.TREES,
        Tile.TREES_TR,
        Tile.TREES_TL,
        Tile.TREES_BR,
        Tile.TREES_BL,
    )
)


def is_tile_collidable(tile):
    if tile in COLLIDEABLE_TILES:
        return True
    return False


TRANSPARENT_TILES = set(
    (
        Tile.EXIT,
        Tile.SPIKES,
        Tile.PIPE,
        Tile.PIPE_TOP,
        Tile.BLOCK,
        Tile.COIN_BLOCK,
    )
)


def is_tile_transparent(tile):
    if tile in TRANSPARENT_TILES:
        return True
    return False


TILE_TEXTURE_SAMPLE_POSITIONS = {
    Tile.AIR: glm.uvec2(0, 0),
    Tile.CAPPED_DIRT: glm.uvec2(0, 1),
    Tile.DIRT: glm.uvec2(1, 1),
    Tile.EXIT: glm.uvec2(0, 9),
    Tile.SPIKES: glm.uvec2(0, 6),
    Tile.PIPE: glm.uvec2(3, 1),
    Tile.PIPE_TOP: glm.uvec2(2, 1),
    Tile.BLOCK: glm.uvec2(4, 1),
    Tile.COIN_BLOCK: glm.uvec2(5, 1),
}


def get_tile_texture_sample_position(tile) -> glm.uvec2:
    return TILE_TEXTURE_SAMPLE_POSITIONS[tile]


def collidable_tile_in_list(tiles):
    for tile in tiles:
        collided = is_tile_collidable(tile)
        if collided:
            return True
    return False
