from enum import Enum, auto
import inspect
from pprint import pprint
import random

import glm

from src.sprites.sprite_animator import BasicSpriteAnimator
from src.sprites.sprite_definitions import FLOWER, MINI_HILL
from src.stage import Decoration
from src.tiles import TILE_SIZE, Tile, is_tile_collidable


def fill_area_with(tiles, tl, br, tile):
    for y in range(tl.y, br.y):
        for x in range(tl.x, br.x):
            # skip if dx dy not in destination size
            if x < 0 or x >= len(tiles):
                continue
            if y < 0 or y >= len(tiles[0]):
                continue
            tiles[y][x] = tile
    return tiles


from src.screens.screens import LETTER_TO_TILE_KEY


def parse_map_tiles_string(map_tiles_string, definition_line_number=0):
    valid_chars = set(LETTER_TO_TILE_KEY.keys())
    rows = []
    for li, line in enumerate(map_tiles_string.strip().splitlines()):
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        # Check if line has the expected width
        if len(line) != 16:
            raise Exception(
                f"Line {li + definition_line_number} length {len(line)} != 16"
            )

        row = []
        for c in line:
            if c not in valid_chars:
                raise Exception(
                    f"unknown tile key '{c}' on line {li + definition_line_number}"
                )
            row.append(LETTER_TO_TILE_KEY[c])
        rows.append(row)

    # Check the number of rows is 11
    if len(rows) != 11:
        raise Exception(f"Expected 11 rows, got {len(rows)}")
    return rows


if __name__ == "__main__":
    _test_tiles_ = """
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
rrrrrrrrrrrrrrrr
"""
    tiles = parse_map_tiles_string(_test_tiles_)
    pprint(tiles)
