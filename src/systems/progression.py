from src.entity import EntityType
from src.state import State

EDGE_THRESHOLD = 2


def check_stage_edge(state: State):
    # Assume there is only one player entity
    try:
        player = next(e for e in state.stage.entities if e.type == EntityType.PLAYER)
    except StopIteration:
        return

    stage = state.stage

    # Left edge: works if player.x is less than threshold
    if player.pos.x < EDGE_THRESHOLD and stage.left_stage:
        state.stage.load_from_screen_data(stage.left_stage)
        state.stage.entities.append(player)
        player.pos.x = state.stage.get_width() - player.size.x - EDGE_THRESHOLD

    # Right edge: check if player's right side exceeds stage width minus threshold
    elif (
        player.pos.x + player.size.x > stage.get_width() - EDGE_THRESHOLD
        and stage.right_stage
    ):
        state.stage.load_from_screen_data(stage.right_stage)
        state.stage.entities.append(player)
        player.pos.x = EDGE_THRESHOLD

    # Top edge: check if player.y is less than threshold
    if player.pos.y < EDGE_THRESHOLD and stage.up_stage:
        state.stage.load_from_screen_data(stage.up_stage)
        state.stage.entities.append(player)
        player.pos.y = state.stage.get_height() - player.size.y - EDGE_THRESHOLD

    # Bottom edge: check if player's bottom exceeds stage height minus threshold
    elif (
        player.pos.y + player.size.y > stage.get_height() - EDGE_THRESHOLD
        and stage.down_stage
    ):
        state.stage.load_from_screen_data(stage.down_stage)
        state.stage.entities.append(player)
        player.pos.y = EDGE_THRESHOLD
