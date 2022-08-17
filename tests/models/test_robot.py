import pytest

from models.platform import Platform
from models.robot import Robot
from utils.enums import Direction


class TestRobot:
    @pytest.fixture
    def robot_platform_fixture(self):
        return Platform(platform_height=5, platform_width=5)

    @pytest.fixture
    def robot_fixture(self, robot_platform_fixture):
        test_robot = Robot()
        test_robot.place(
            x_axis=0,
            y_axis=0,
            facing=Direction.NORTH.name,
            platform=robot_platform_fixture,
        )
        return test_robot

    @pytest.mark.parametrize(
        "x_axis, y_axis, face",
        [
            (1, 1, Direction.NORTH.name),
            (1, 2, Direction.SOUTH.name),
        ],
    )
    def test_place(self, robot_platform_fixture, x_axis, y_axis, face):
        test_robot = Robot()
        test_robot.place(
            x_axis=x_axis,
            y_axis=y_axis,
            facing=face,
            platform=robot_platform_fixture,
        )

        assert test_robot.x_axis == x_axis
        assert test_robot.y_axis == y_axis
        assert test_robot.facing == face
        assert test_robot.platform == robot_platform_fixture

    @pytest.mark.parametrize(
        "x_axis, y_axis, face",
        [
            (6, 6, Direction.NORTH.name),
            (10, 10, Direction.SOUTH.name),
        ],
    )
    def test_not_place(self, robot_platform_fixture, x_axis, y_axis, face):

        test_robot = Robot()
        test_robot.place(
            x_axis=x_axis,
            y_axis=y_axis,
            facing=face,
            platform=robot_platform_fixture,
        )
        assert test_robot.x_axis is None
        assert test_robot.y_axis is None
        assert test_robot.facing is None
        assert test_robot.platform is None

    @pytest.mark.parametrize(
        "platform, current_face, expected_face",
        [
            (
                robot_platform_fixture,
                Direction.EAST.name,
                Direction.NORTH.name,
            ),
            (
                robot_platform_fixture,
                Direction.SOUTH.name,
                Direction.EAST.name,
            ),
            (
                robot_platform_fixture,
                Direction.WEST.name,
                Direction.SOUTH.name,
            ),
            (
                robot_platform_fixture,
                Direction.NORTH.name,
                Direction.WEST.name,
            ),
            (None, Direction.NORTH.name, Direction.NORTH.name),
        ],
    )
    def test_left(self, robot_fixture, platform, current_face, expected_face):
        if not platform:
            robot_fixture.platform = platform
        robot_fixture.facing = current_face
        robot_fixture.left()
        assert robot_fixture.facing == expected_face

    @pytest.mark.parametrize(
        "platform, current_face, expected_face",
        [
            (
                robot_platform_fixture,
                Direction.NORTH.name,
                Direction.EAST.name,
            ),
            (
                robot_platform_fixture,
                Direction.EAST.name,
                Direction.SOUTH.name,
            ),
            (
                robot_platform_fixture,
                Direction.SOUTH.name,
                Direction.WEST.name,
            ),
            (
                robot_platform_fixture,
                Direction.WEST.name,
                Direction.NORTH.name,
            ),
            (None, Direction.NORTH.name, Direction.NORTH.name),
        ],
    )
    def test_right(self, robot_fixture, platform, current_face, expected_face):
        if not platform:
            robot_fixture.platform = platform
        robot_fixture.facing = current_face
        robot_fixture.right()
        assert robot_fixture.facing == expected_face

    @pytest.mark.parametrize(
        "platform, face, expected_x_axis, expected_y_axis",
        [
            (robot_platform_fixture, Direction.NORTH.name, 0, 1),
            (robot_platform_fixture, Direction.EAST.name, 1, 0),
            (robot_platform_fixture, Direction.SOUTH.name, 0, 0),
            (robot_platform_fixture, Direction.WEST.name, 0, 0),
            (None, Direction.NORTH.name, 0, 0),
        ],
    )
    def test_move(
        self, robot_fixture, platform, face, expected_x_axis, expected_y_axis
    ):
        if not platform:
            robot_fixture.platform = platform
        robot_fixture.facing = face
        robot_fixture.move()

        assert robot_fixture.x_axis == expected_x_axis
        assert robot_fixture.y_axis == expected_y_axis

    def test_report(self, robot_fixture):
        x_axis, y_axis, face = robot_fixture.report()
        assert x_axis == robot_fixture.x_axis
        assert y_axis == robot_fixture.y_axis
        assert face == robot_fixture.facing
