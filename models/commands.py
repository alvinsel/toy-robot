import re

from config import Config
from models.robot import Robot
from models.platform import Platform


class CommandParser:
    @staticmethod
    def parse_command(command):
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


class RobotCommand:
    """Command base class"""

    def __init__(self, command):
        self.command = command

    def invoke(self, *args, **kwargs):
        """Executes the commands in the sub classes"""
        return


class PlaceCommand(RobotCommand):
    def invoke(self, *args, **kwargs):
        robot = kwargs.get("robot")
        platform = kwargs.get("platform")

        # Validates if robot and platform is existing
        if not robot and not platform:
            return

        # Makes sure if robot and platform is the right type
        if not isinstance(robot, Robot) or not isinstance(platform, Platform):
            return

        # Regex Command Check
        result = re.search(Config.PLACE_PATTERN, self.command)
        if not result:
            return

        # Put valid commands in variables
        x_axis, y_axis, facing = (
            int(result.group(2)),
            int(result.group(3)),
            result.group(4),
        )

        # Place the robot object
        kwargs.get("robot").place(
            x_axis=x_axis, y_axis=y_axis, facing=facing, platform=platform
        )


class MoveCommand(RobotCommand):
    def invoke(self, *args, **kwargs):
        robot = kwargs.get("robot")

        # Makes sure if robot is the right type
        if not robot or not isinstance(robot, Robot):
            return

        # Move the robot object towards the direction he is facing
        robot.move()


class LeftCommand(RobotCommand):
    def invoke(self, *args, **kwargs):
        robot = kwargs.get("robot")

        # Makes sure if robot is the right type
        if not robot or not isinstance(robot, Robot):
            return

        # Move the robot face to the left
        robot.left()


class RightCommand(RobotCommand):
    def invoke(self, *args, **kwargs):
        robot = kwargs.get("robot")

        # Makes sure if robot is the right type
        if not robot or not isinstance(robot, Robot):
            return

        # Move the robot face to the right
        robot.right()


class ReportCommand(RobotCommand):
    def invoke(self, *args, **kwargs):
        robot = kwargs.get("robot")

        # Makes sure if robot is the right type
        if not robot or not isinstance(robot, Robot):
            return

        # Show the robot state
        robot.report()
