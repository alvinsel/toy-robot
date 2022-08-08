class Config:
    """Default configurations for toy robot"""

    PLATFORM_SIZE_X = 5  # X Axis
    PLATFORM_SIZE_Y = 5  # Y Axis

    PLACE_PATTERN = r"^(PLACE)\s([0-9]+)\,([0-9]+)\,(NORTH|EAST|SOUTH|WEST)$"
