from models.platform import Platform
from utils.enums import Direction, Movement, Rotation


class Robot(object):
    def __init__(
        self,
    ):
        self.x_axis = None
        self.y_axis = None
        self.facing = None
        self.platform = None

    def place(self, x_axis: int, y_axis: int, facing: str, platform: Platform) -> None:
        """Sets the robot initial state"""
        if platform:
            if platform.is_coordinate_available(x_axis=x_axis, y_axis=y_axis):
                self.x_axis = x_axis
                self.y_axis = y_axis
                self.facing = facing
                self.platform = platform

    def left(self):
        """Face the Robot face to the right (North -> West -> South -> East)"""
        # Check if platform is available
        if self.platform:
            self.rotate(Rotation.LEFT)

    def right(self):
        """Face the Robot face to the right (North -> East -> South -> West)"""
        # Check if platform is available
        if self.platform:
            self.rotate(Rotation.RIGHT)

    def move(self):
        """Moves the robot towards the direction it's facing"""
        # Check if platform is available
        if self.platform:
            # Add the coordinate depending on the config numbers
            x_axis_value, y_axis_value = Movement[self.facing].value
            new_x_axis = self.x_axis + x_axis_value
            new_y_axis = self.y_axis + y_axis_value

            # Only move when robot will not fall
            if self.platform.is_coordinate_available(
                x_axis=new_x_axis, y_axis=new_y_axis
            ):
                self.x_axis = new_x_axis
                self.y_axis = new_y_axis

    def report(self):
        """Shows the current robot position"""
        # Check if platform is available
        if self.platform:
            print(f"Output:{self.x_axis},{self.y_axis},{self.facing}")
            return self.x_axis, self.y_axis, self.facing

    def rotate(self, rotation: Rotation) -> None:
        """Face robot to the giver rotation command"""
        # Checks the current direction and add numbers referencing to enum for the next direction
        current_face = Direction[self.facing].value
        new_face = (current_face + Rotation(rotation).value) % len(Direction)
        self.facing = Direction(new_face).name
