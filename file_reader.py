import argparse

from config import Config
from models.commands import CommandParser
from models.platform import Platform
from models.robot import Robot


def main():
    robot = Robot()
    platform = Platform(
        platform_height=Config.PLATFORM_SIZE_Y,
        platform_width=Config.PLATFORM_SIZE_X,
    )

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    args = parser.parse_args()
    if args.file.endswith(".txt"):
        with open(args.file) as file:
            for user_input in file:
                command_parser = CommandParser()
                command = command_parser.parse_command(user_input)
                command.invoke(robot=robot, platform=platform)


if __name__ == "__main__":
    main()
