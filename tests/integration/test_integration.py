import os
import pytest

from models.commands import UserCommand
from models.platform import Platform
from models.robot import Robot


class TestIntegration:
    DATA_PATH = f"{os.path.dirname(__file__)}/test_scenarios"
    FILE_NAMES = os.listdir(DATA_PATH)

    @pytest.fixture
    def robot_platform_fixture(self):
        return Platform(platform_height=5, platform_width=5)

    @pytest.fixture
    def robot_fixture(self, robot_platform_fixture):
        return Robot()

    @pytest.mark.parametrize(
        "file_name", [file_name for file_name in FILE_NAMES]
    )
    def test_integration_via_file(
        self, robot_fixture, robot_platform_fixture, file_name: str
    ):
        print(file_name)
        with open(f"{self.DATA_PATH}/{file_name}") as file:
            for user_input in file:
                UserCommand.execute_command(
                    user_input, robot_fixture, robot_platform_fixture
                )
                if user_input.startswith("Output"):
                    assert (
                        user_input
                        == f"Output: {robot_fixture.x_axis},{robot_fixture.y_axis},{robot_fixture.facing}"
                    )
