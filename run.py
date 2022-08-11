import argparse

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

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=False)
    args = parser.parse_args()
    command = None
    if args.file and args.file.endswith(".txt"):
        with open(args.file) as file:
            for user_input in file:
                execute_commands(user_input=user_input, robot=robot, platform=platform)
    else:
        while not isinstance(command, ReportCommand):
            # Get User Input
            user_input = input("Enter command:\t")
            execute_commands(user_input=user_input, robot=robot, platform=platform)


def execute_commands(user_input, robot, platform):
    command_parser = CommandParser()
    command = command_parser.parse_command(user_input)
    command.invoke(robot=robot, platform=platform)


if __name__ == "__main__":
    main()