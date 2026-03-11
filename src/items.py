import glm
from sprites.sprite_definitions import SLAP
from src.special_effect import SpecialEffect
from src.entity import Entity, Facing, get_entity_bounds
from src.state import State
from src.sprites.sprite_animator import SpriteAnimator


class Item:
    def __init__(self) -> None:
        self.name = "Item"
        self.unlimited = False
        self.max_quantity = 100
        self.quantity = 100
        self.cooldown = 0.5
        self.timer = 0
        self.use_function = None
        self.droppable = False

    def step(self, dt):
        if self.timer > 0:
            self.timer -= dt

        if self.timer < 0:
            self.timer = 0

    def full_refill(self):
        self.quantity = self.max_quantity

    def refill(self, amount):
        self.quantity += amount
        if self.quantity > self.max_quantity:
            self.quantity = self.max_quantity

    def post_use(self):
        if not self.unlimited:
            self.quantity -= 1
        self.timer = self.cooldown
        print(f"Used {self.name}")

    def can_use(self):
        if self.timer != 0:
            return False
        if not self.unlimited and self.quantity == 0:
            return False
        if not self.use_function:
            return False
        return True


class WhiteGlove(Item):
    def __init__(self) -> None:
        super().__init__()
        self.name = "White Glove"
        self.cooldown = 0.5
        self.timer = 0
        self.size = glm.vec2(2, 2)
        self.range = 6
        self.stun_duration = 1

    def use(self, state: State, user: Entity) -> False:
        if not self.can_use():
            return False
        self.post_use()

        # calculate position
        user_pos = user.get_center()
        facing = user.facing
        direction = glm.vec2(0, 0)
        match = {
            Facing.UP: glm.vec2(0, -1),
            Facing.DOWN: glm.vec2(0, 1),
            Facing.LEFT: glm.vec2(-1, 0),
            Facing.RIGHT: glm.vec2(1, 0),
        }
        direction = match[facing]
        use_pos = user_pos + direction * self.range
        use_tl, use_br = get_entity_bounds(use_pos, self.size)

        # get all enemies in an area
        hit_entities = []
        for entity in state.entities:
            if entity == user:
                continue
            if entity.intersects_area(use_tl, use_br):
                hit_entities.append(entity)

        # if its an interactable, interact with it
        for entity in hit_entities:
            if entity.interactable:
                entity.interact(state, user)

        # if its a stunnable, stun it
        for entity in hit_entities:
            if entity.stun_timer == 0:
                entity.stun_timer = self.stun_duration
                entity.vel = glm.vec2(0, 0)
                entity.acc = glm.vec2(0, 0)
                print(f"Stunned {entity}")

        # spawn a slap particle effect
        slap_effect = SpecialEffect(
            0.2,
            use_pos,
            glm.vec2(2, 2),
            SpriteAnimator(
                SLAP,
            ),
        )
        state.special_effects.append(slap_effect)
