from enum import Enum, auto

import glm

from src.graphics import Textures
from src.sprites.serially_stored_animated_sprite import SeriallyStoredAnimatedSprite
from src.sprites.sprite import Sprite
from src.sprites.static_sprite import StaticSprite

###################################################################################
##########################    ENTITY STUFF                 ########################
###################################################################################
# ////////////////////////    ENTITY SPRITE DEFINITIONS    ////////////////////////
DEFAULT = StaticSprite(
    Textures.ENTITIES,
    glm.vec2(0, 48),
    glm.vec2(16, 16),
)

PLAYER_DOWN = SeriallyStoredAnimatedSprite(
    Textures.ENTITIES,
    glm.vec2(0, 112),
    glm.vec2(16, 16),
    glm.vec2(-2, 0),
    2,
    True,
)

PLAYER_LEFT = SeriallyStoredAnimatedSprite(
    Textures.ENTITIES,
    glm.vec2(0, 128),
    glm.vec2(16, 16),
    glm.vec2(-2, 0),
    2,
    True,
)


PLAYER_UP = SeriallyStoredAnimatedSprite(
    Textures.ENTITIES,
    glm.vec2(0, 144),
    glm.vec2(16, 16),
    glm.vec2(0, 0),
    2,
    True,
)

PLAYER_PUNCH = StaticSprite(
    Textures.ENTITIES,
    glm.vec2(38, 120),
    glm.vec2(4, 3),
)

GOOMBA_WALKING = SeriallyStoredAnimatedSprite(
    Textures.ENTITIES,
    glm.vec2(64, 16),
    glm.vec2(16, 16),
    glm.vec2(-2, -2),
    4,
    True,
)

GOOMBA_DEAD = SeriallyStoredAnimatedSprite(
    Textures.ENTITIES,
    glm.vec2(64, 32),
    glm.vec2(16, 16),
    glm.vec2(-2, -5),
    11,
    False,
)

GOOMBINI_WALKING = SeriallyStoredAnimatedSprite(
    Textures.ENTITIES,
    glm.vec2(64, 48),
    glm.vec2(16, 16),
    glm.vec2(-5, -9),
    4,
    True,
)

GOOMBINI_DEAD = SeriallyStoredAnimatedSprite(
    Textures.ENTITIES,
    glm.vec2(64, 64),
    glm.vec2(16, 16),
    glm.vec2(-5, -11),
    11,
    False,
)

GOOMBOR_WALKING = SeriallyStoredAnimatedSprite(
    Textures.ENTITIES,
    glm.vec2(64, 80),
    glm.vec2(32, 32),
    glm.vec2(-4, -4),
    4,
    True,
)

GOOMBOR_DEAD = SeriallyStoredAnimatedSprite(
    Textures.ENTITIES,
    glm.vec2(64, 32),
    glm.vec2(32, 32),
    glm.vec2(-4, -4),
    11,
    False,
)


###################################################################################
##########################    DECORATIONS STUFF            ########################
###################################################################################
# ////////////////////////   DECORATION SPRITE DEFINITIONS ////////////////////////
FLOWER = SeriallyStoredAnimatedSprite(
    Textures.DECORATIONS,
    glm.vec2(0, 0),
    glm.vec2(16, 16),
    glm.vec2(0, 0),
    2,
    True,
)

MINI_HILL = StaticSprite(
    Textures.DECORATIONS,
    glm.vec2(0, 16),
    glm.vec2(16, 16),
)

BIG_PIPE = StaticSprite(
    Textures.DECORATIONS,
    glm.vec2(16, 16),
    glm.vec2(32, 32),
)

SUN = SeriallyStoredAnimatedSprite(
    Textures.DECORATIONS,
    glm.vec2(0, 48),
    glm.vec2(48, 48),
    glm.vec2(0, 0),
    2,
    True,
)
