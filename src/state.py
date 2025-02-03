from enum import Enum, auto
from entity import get_entity_bounds

from stage import Screen


class Mode(Enum):
    PAUSE = auto()
    PLAYING = auto()


class Message:
    def __init__(self, text, lifetime) -> None:
        self.text = text
        self.lifetime = lifetime


def step_and_cleanse(collection):
    for item in collection:
        item.lifetime -= 1
    return [item for item in collection if item.lifetime > 0]


class State:
    def __init__(self) -> None:
        self.mode = Mode.PLAYING

        self.screen: Screen = None
        self.entities = []

        self.events = []
        self.special_effects = []

        self.debug_messages: list[str] = []
        self.alerts: list[Message] = []

        self.center_cam_on_player = True

    def load_screen(self, screen):
        self.screen = screen
        self.entities = screen.entities

    def step_alerts(self):
        self.alerts = step_and_cleanse(self.alerts)
