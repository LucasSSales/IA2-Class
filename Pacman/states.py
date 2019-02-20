from enum import Enum


class State(Enum):
    MAIN_MENU = 0
    PLAYING = 1
    GAME_OVER = 2

class AgentState(Enum):
    SEARCH = 0
    STAL = 1