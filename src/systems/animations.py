from src.graphics import Graphics
from src.sprites.sprite_definitions import PLAYER_DOWN, PLAYER_LEFT, PLAYER_UP
from src.entity import EntityType, Facing, get_entity_bounds
from src.sprites.sprite_animator import DEFAULT_FRAME_DURATION
from src.tiles import TILE_SIZE
from src.state import State


def step_sprite_animators(state: State, graphics: Graphics):
    for e in state.stage.entities:
        if e.sprite_animator is not None:
            e.sprite_animator.step()

    cam_l = graphics.camera.pos.x
    cam_r = graphics.camera.pos.x + graphics.camera.size.x

    # for d in state.foreground_decorations:
    #     if d.sprite_animator is not None:
    #         if d.pos.x > cam_r:
    #             continue
    #         if (d.pos.x + TILE_SIZE * 2) < cam_l:
    #             continue
    #         d.sprite_animator.step()


FACING_THRESHOLD = 1.0


def set_facing(state: State):
    for entity in state.stage.entities:
        # if all velocities are under threshold, don't change facing
        if (
            abs(entity.vel.x) < FACING_THRESHOLD
            and abs(entity.vel.y) < FACING_THRESHOLD
        ):
            continue

        if entity.vel.x > FACING_THRESHOLD:
            entity.facing = Facing.RIGHT
        elif entity.vel.x < -FACING_THRESHOLD:
            entity.facing = Facing.LEFT
        elif entity.vel.y > FACING_THRESHOLD:
            entity.facing = Facing.DOWN
        elif entity.vel.y < -FACING_THRESHOLD:
            entity.facing = Facing.UP


def set_facing_sprite_for_non_rotators(state: State):
    for entity in state.stage.entities:
        if entity.rotate_to_facing:
            continue

        if entity.type == EntityType.PLAYER:
            if entity.facing == Facing.LEFT or entity.facing == Facing.RIGHT:
                entity.sprite_animator.set_sprite(PLAYER_LEFT)
            elif entity.facing == Facing.UP:
                entity.sprite_animator.set_sprite(PLAYER_UP)
            elif entity.facing == Facing.DOWN:
                entity.sprite_animator.set_sprite(PLAYER_DOWN)


WALKING_THRESHOLD = 1.5
RUNNING_THRESHOLD = 2.5
