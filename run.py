from config import Config
from models.commands import CommandParser, ReportCommand
from models.platform import Platform
from models.robot import Robot


def main():
    robot = Robot()
    platform = Platform(
        platform_height=Config.PLATFORM_SIZE_Y,
        platform_width=Config.PLATFORM_SIZE_X,
    )
    command = None

    while not isinstance(command, ReportCommand):
        # Get User Input
        user_input = input("Enter command:\t")
        command_parser = CommandParser()
        command = command_parser.parse_command(user_input)
        command.invoke(robot=robot, platform=platform)


if __name__ == "__main__":
    main()
