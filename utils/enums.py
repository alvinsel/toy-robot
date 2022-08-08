from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Movement(Enum):
    NORTH = 0, 1
    EAST = 1, 0
    SOUTH = 0, -1
    WEST = -1, 0


class Rotation(Enum):
    LEFT = -1
    RIGHT = 1


class Commands(Enum):
    """Valid Commands"""

    LEFT = "LEFT"
    RIGHT = "RIGHT"
    MOVE = "MOVE"
    REPORT = "REPORT"
    PLACE = "PLACE"
