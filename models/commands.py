import re

from config import Config
from models.platform import Platform
from models.robot import Robot


class RobotCommand:
    """Command base class"""

    def __init__(self, command: str) -> None:
        self.command = command

    def invoke(self, *args, **kwargs):
        """Executes the commands in the subclasses"""
        robot = kwargs.get("robot")
        if not robot or not isinstance(robot, Robot):
            raise ValueError("NO ROBOT FOUND")
        return


class PlaceCommand(RobotCommand):
    def invoke(self, *args, **kwargs):
        super().invoke(*args, **kwargs)
        platform = kwargs.get("platform")

        # Makes sure if robot and platform is the right type
        if not platform or not isinstance(platform, Platform):
            raise ValueError("NO PLATFORM FOUND")

        # Regex Command Check
        result = re.search(Config.PLACE_PATTERN, self.command)
        if not result:
            return None
        # Put valid commands in variables
        x_axis, y_axis, facing = (
            int(result.group(2)),
            int(result.group(3)),
            result.group(4),
        )

        # Place the robot object
        kwargs["robot"].place(
            x_axis=x_axis, y_axis=y_axis, facing=facing, platform=platform
        )


class MoveCommand(RobotCommand):
    def invoke(self, *args, **kwargs):
        super().invoke(*args, **kwargs)
        # Move the robot object towards the direction he is facing
        kwargs["robot"].move()


class LeftCommand(RobotCommand):
    def invoke(self, *args, **kwargs):
        super().invoke(*args, **kwargs)
        # Move the robot face to the left
        kwargs["robot"].left()


class RightCommand(RobotCommand):
    def invoke(self, *args, **kwargs):
        super().invoke(*args, **kwargs)
        # Move the robot face to the right
        kwargs["robot"].right()


class ReportCommand(RobotCommand):
    def invoke(self, *args, **kwargs):
        super().invoke(*args, **kwargs)
        # Show the robot state
        kwargs["robot"].report()


class UserCommand:
    @staticmethod
    def execute_command(user_input: str, robot: Robot, platform: Platform) -> None:
        command = UserCommand.parse_command(user_input)
        command.invoke(robot=robot, platform=platform)

    @staticmethod
    def parse_command(command: str) -> RobotCommand:
        """Checks the user input command and return the right class"""
        initial_token = command.strip()
        if initial_token:
            initial_token = command.split()[0]
        commands = {
            "PLACE": PlaceCommand(command),
            "MOVE": MoveCommand(command),
            "LEFT": LeftCommand(command),
            "RIGHT": RightCommand(command),
            "REPORT": ReportCommand(command),
        }
        return commands.get(initial_token, RobotCommand(command))

