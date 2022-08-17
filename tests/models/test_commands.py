from unittest.mock import Mock

import pytest

from models.commands import UserCommand
from models.platform import Platform
from models.robot import Robot
from utils.enums import Direction, Commands


class TestCommand:
    @pytest.fixture
    def robot_platform_fixture(self):
        return Mock(spec=Platform)

    @pytest.fixture
    def robot_fixture(self):
        mock_robot = Mock(spec=Robot)
        mock_robot.left = Mock()
        mock_robot.right = Mock()
        mock_robot.move = Mock()
        mock_robot.report = Mock()
        mock_robot.place = Mock()
        mock_robot.actions = {
            "left": mock_robot.left,
            "right": mock_robot.right,
            "move": mock_robot.move,
            "report": mock_robot.report,
            "place": mock_robot.place,
        }
        return mock_robot

    @pytest.mark.parametrize(
        "user_command, expected_call",
        [
            (Commands.LEFT.name, "left"),
            (Commands.RIGHT.name, "right"),
            (Commands.MOVE.name, "move"),
            (Commands.REPORT.name, "report"),
            (f"{Commands.PLACE.name} 0,0,{Direction.NORTH.name}", "place"),
        ],
    )
    def test_command_parser(
        self,
        user_command,
        expected_call,
        robot_fixture,
        robot_platform_fixture,
    ):
        command = UserCommand.parse_command(user_command)
        command.invoke(robot=robot_fixture, platform=robot_platform_fixture)

        robot_fixture.actions[expected_call].assert_called()

    @pytest.mark.parametrize(
        "user_command",
        ["NOTACOMMAND", "XXXMOVE", "PLACE", "PLACE notInt,2,NORTH"],
    )
    def test_command_parser_no_action(
        self, user_command, robot_fixture, robot_platform_fixture
    ):
        command = UserCommand.parse_command(user_command)
        command.invoke(robot=robot_fixture, platform=robot_platform_fixture)

        for action, _ in robot_fixture.actions.items():
            assert not robot_fixture.actions[action].called

    @pytest.mark.parametrize(
        "user_command, expected_call",
        [
            (Commands.LEFT.name, "left"),
            (Commands.RIGHT.name, "right"),
            (Commands.MOVE.name, "move"),
            (Commands.REPORT.name, "report"),
            (f"{Commands.PLACE.name} 0,0,{Direction.NORTH.name}", "place"),
        ],
    )
    def test_command_parser_no_robot_or_platform(
        self, user_command, expected_call, robot_fixture
    ):
        with pytest.raises(ValueError):
            command = UserCommand.parse_command(user_command)
            command.invoke(robot=None, platform=None)

    def test_command_parser_place_with_robot_no_platform(self, robot_fixture):
        with pytest.raises(ValueError):
            command = UserCommand.parse_command(
                f"{Commands.PLACE.name} 0,0,{Direction.NORTH.name}"
            )
            command.invoke(robot=robot_fixture, platform="NotAPlatform")
