import glm

from src.graphics import Graphics
from src.entity import EntityType
from src.tiles import TILE_SIZE
from src.state import State


def control_camera(state, graphics):
    cam_speed = 1

    if state.inputs.camera_left:
        graphics.camera.pos.x -= cam_speed
    if state.inputs.camera_right:
        graphics.camera.pos.x += cam_speed
    if state.inputs.camera_up:
        graphics.camera.pos.y -= cam_speed
    if state.inputs.camera_down:
        graphics.camera.pos.y += cam_speed


def center_cam_on_player(state: State, graphics: Graphics):
    if not state.center_cam_on_player:
        return
    player_entities = [e for e in state.stage.entities if e.type == EntityType.PLAYER]
    if not player_entities:
        return

    xs = [e.pos.x + e.size.x / 2 for e in player_entities]
    ys = [e.pos.y + e.size.y / 2 for e in player_entities]
    x = int(sum(xs) / len(xs)) + TILE_SIZE // 2
    y = int(sum(ys) / len(ys)) + TILE_SIZE // 2
    p = glm.vec2(x, y)
    graphics.camera.set_center(p)

    # Clamp camera in the x dimension
    if state.stage.wc_dims.x >= graphics.camera.size.x:
        if graphics.camera.pos.x < 0:
            graphics.camera.pos.x = 0
        cam_right_edge = graphics.camera.pos.x + graphics.camera.size.x
        stage_right_edge = state.stage.wc_dims.x + TILE_SIZE
        if cam_right_edge > stage_right_edge:
            graphics.camera.pos.x = stage_right_edge - graphics.camera.size.x

    # Clamp camera in the y dimension
    if state.stage.wc_dims.y >= graphics.camera.size.y:
        if graphics.camera.pos.y < 0:
            graphics.camera.pos.y = 0
        cam_bottom_edge = graphics.camera.pos.y + graphics.camera.size.y
        stage_bottom_edge = state.stage.wc_dims.y + TILE_SIZE
        if cam_bottom_edge > stage_bottom_edge:
            graphics.camera.pos.y = stage_bottom_edge - graphics.camera.size.y


WALK_FORCE = 0.3
RUN_FORCE = 0.5
JUMP_FORCE = -3.6
RUNNING_JUMP_FORCE = -4.8


def control_entities(state):
    controllable_entities = [e for e in state.stage.entities if e.input_controlled]
    for e in controllable_entities:
        if state.inputs.left:
            e.acc.x -= WALK_FORCE
        if state.inputs.right:
            e.acc.x += WALK_FORCE
        if state.inputs.down:
            e.acc.y += WALK_FORCE
        if state.inputs.up:
            e.acc.y -= WALK_FORCE


no_move_force = 0.8
WALKING_MAX_SPEED = 1.0


def speed_limit_controlled_entities(state):
    controllable_entities = [e for e in state.stage.entities if e.input_controlled]

    for e in controllable_entities:
        if e.input_controlled:
            if state.inputs.right:
                e.vel.x = min(e.vel.x, WALKING_MAX_SPEED)
            else:
                # slow down
                if e.vel.x > 0:
                    e.acc.x = max(-no_move_force, -e.vel.x)
                pass

            if state.inputs.left:
                e.vel.x = max(e.vel.x, -WALKING_MAX_SPEED)
            else:
                # slow down
                if e.vel.x < 0:
                    e.acc.x = max(no_move_force, e.vel.x)

            if state.inputs.up:
                e.vel.y = max(e.vel.y, -WALKING_MAX_SPEED)
            else:
                # slow down
                if e.vel.y < 0:
                    e.acc.y = max(no_move_force, e.vel.y)

            if state.inputs.down:
                e.vel.y = min(e.vel.y, WALKING_MAX_SPEED)
            else:
                # slow down
                if e.vel.y > 0:
                    e.acc.y = max(-no_move_force, -e.vel.y)
