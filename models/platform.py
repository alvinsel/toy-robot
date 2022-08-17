class Platform(object):
    def __init__(self, platform_height: int, platform_width: int):
        self.platform_height = platform_height - 1
        self.platform_width = platform_width - 1

    def is_coordinate_available(self, x_axis: int, y_axis: int) -> bool:
        if (
            self.platform_height >= y_axis >= 0
            and self.platform_width >= x_axis >= 0
        ):
            return True

        return False
