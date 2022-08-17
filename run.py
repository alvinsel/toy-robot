import argparse

from config import Config
from models.commands import UserCommand
from models.platform import Platform
from models.robot import Robot
from utils.enums import Commands


def main():
    robot = Robot()
    platform = Platform(
        platform_height=Config.PLATFORM_SIZE_Y,
        platform_width=Config.PLATFORM_SIZE_X,
    )

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=False)
    args = parser.parse_args()
    user_input = None
    if args.file and args.file.endswith(".txt"):
        with open(args.file) as file:
            for user_input in file:
                execute(user_input=user_input, robot=robot, platform=platform)
    else:
        while user_input != Commands.REPORT.value:
            # Get User Input
            user_input = input("Enter command:\t")

            execute(user_input=user_input, robot=robot, platform=platform)


def execute(user_input: str, robot: Robot, platform: Platform) -> None:
    try:
        UserCommand.execute_command(
            user_input=user_input, robot=robot, platform=platform
        )
    except ValueError:
        # Ignoring Command
        pass


if __name__ == "__main__":
    main()
