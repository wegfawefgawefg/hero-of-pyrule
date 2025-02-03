import pygame

from src.audio import handle_audio_events
from src.entity import EntityType
from src.events import handle_events
from src.render import mouse_pos
from src.state import Mode
from src.systems.ai import step_ai
from src.systems.animations import (
    set_facing,
    set_facing_sprite_for_non_rotators,
    step_sprite_animators,
)
from src.systems.control import (
    center_cam_on_player,
    control_camera,
    control_entities,
    speed_limit_controlled_entities,
)
from src.systems.debug import debug_collisions
from src.systems.physics import (
    physics_post_step,
    zero_accelerations,
)
from src.systems.progression import check_stage_edge


def step_playing(state, graphics, audio):

    #### PRE STEP
    # control_camera(state, graphics)
    # update_display_states(state)
    zero_accelerations(state)

    ### STEP
    control_entities(state)
    step_ai(state, graphics, audio)

    ### POST STEP
    speed_limit_controlled_entities(state)
    physics_post_step(state)

    set_facing(state)
    set_facing_sprite_for_non_rotators(state)
    step_sprite_animators(state, graphics)

    center_cam_on_player(state, graphics)
    check_stage_edge(state)

    # some_debug_messages(state, graphics)
    # debug_collisions(state)


def some_debug_messages(state, graphics):
    # print player position
    player_entities = [e for e in state.stage.entities if e.type == EntityType.PLAYER]
    if len(player_entities) > 0:
        player = player_entities[0]
        state.debug_messages.append(f"player pos: {player.pos}")

    # print cam position
    state.debug_messages.append(f"cam pos: {graphics.camera.pos}")
    # print cam center
    state.debug_messages.append(f"cam center: {graphics.camera.get_center()}")

    # player facing
    state.debug_messages.append(f"player facing: {player.facing}")

    # player vel
    state.debug_messages.append(f"player vel: {player.vel}")

    # print coyote timer
    if len(player_entities) > 0:
        player = player_entities[0]
        state.debug_messages.append(f"coyote timer: {player.coyote_timer.timer}")

    # print mouse pos
    state.debug_messages.append(f"mouse pos: {mouse_pos(graphics)}")


def step_pause(state, graphics):
    pass


def step(state, graphics, audio):
    state.step_alerts()
    state.debug_messages.clear()
    state.events.clear()

    match state.mode:
        case Mode.PLAYING:
            step_playing(state, graphics, audio)
        case Mode.PAUSE:
            step_pause(state, graphics)

    handle_events(state, graphics, audio)
    handle_audio_events(audio)
