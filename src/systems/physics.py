import glm

from src.collisions import (
    do_collisions_horizontal,
    do_collisions_vertical,
    do_entity_collisions_horizontal,
    do_entity_collisions_vertical,
)
from src.entity import get_entity_bounds, get_entity_feet, intersects
from src.tiles import TILE_SIZE, collidable_tile_in_list


def zero_accelerations(state):
    for e in state.stage.entities:
        e.acc = glm.vec2(0, 0)


MAX_SPEED = 6.0


def physics_post_step(state):
    for e in state.stage.entities:
        e.vel += e.acc

        # clamp
        if e.vel.x > MAX_SPEED:
            e.vel.x = MAX_SPEED
        elif e.vel.x < -MAX_SPEED:
            e.vel.x = -MAX_SPEED
        if e.vel.y > MAX_SPEED:
            e.vel.y = MAX_SPEED
        elif e.vel.y < -MAX_SPEED:
            e.vel.y = -MAX_SPEED

        if e.has_tile_collisions or e.has_entity_collisions:
            #   vertical
            t_new_y = None
            e_new_y = None
            if e.has_tile_collisions:
                t_new_y = do_collisions_vertical(state, e, e.pos, e.size, e.vel)
            if e.has_entity_collisions:
                e_new_y = do_entity_collisions_vertical(state, e, e.pos, e.size, e.vel)
            if t_new_y is None and e_new_y is None:
                e.pos.y += e.vel.y
            else:
                if t_new_y is None and e_new_y is not None:
                    e.pos.y = e_new_y
                    e.vel.y = 0.0
                elif t_new_y is not None and e_new_y is None:
                    e.pos.y = t_new_y
                    e.vel.y = 0.0
                else:
                    if e.vel.y > 0:
                        e.pos.y = min(t_new_y, e_new_y)
                        e.vel.y = 0.0
                    elif e.vel.y < 0:  # MAYBE BUG: when not moving
                        e.pos.y = max(t_new_y, e_new_y)
                        e.vel.y = 0.0

            #   horizontal
            t_new_x = None
            e_new_x = None
            if e.has_tile_collisions:
                t_new_x = do_collisions_horizontal(state, e, e.pos, e.size, e.vel)
            if e.has_entity_collisions:
                e_new_x = do_entity_collisions_horizontal(
                    state, e, e.pos, e.size, e.vel
                )
            if t_new_x is None and e_new_x is None:
                e.pos.x += e.vel.x
            else:
                if t_new_x is None and e_new_x is not None:
                    e.pos.x = e_new_x
                    e.vel.x = 0.0
                elif t_new_x is not None and e_new_x is None:
                    e.pos.x = t_new_x
                    e.vel.x = 0.0
                else:
                    if e.vel.x > 0:
                        e.pos.x = min(t_new_x, e_new_x)
                        e.vel.x = 0.0
                    elif e.vel.x < 0:  # MAYBE BUG: when not moving
                        e.pos.x = max(t_new_x, e_new_x)
                        e.vel.x = 0.0

        else:
            e.pos += e.vel
