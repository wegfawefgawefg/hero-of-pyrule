from __future__ import annotations

import glm

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.sprites.sprite_animator import SpriteAnimator


class SpecialEffect:
    def __init__(
        self,
        lifetime: float,
        pos: glm.vec2,
        size: glm.vec2,
        sprite_animator=None,
    ):
        self.lifetime = lifetime
        self.pos = pos
        self.size = size
        self.sprite_animator: SpriteAnimator = sprite_animator

    def step(self, dt: float):
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.lifetime = 0

        self.sprite_animator.step()
