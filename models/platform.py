from dataclasses import dataclass


@dataclass
class Platform:
    platform_height: int
    platform_width: int

    def max_x(self) -> int:
        return self.platform_width - 1

    def max_y(self) -> int:
        return self.platform_height - 1
