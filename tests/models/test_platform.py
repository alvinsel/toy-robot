import pytest

from models.platform import Platform


class TestPlatform:
    @pytest.fixture
    def robot_platform_fixture(self):
        return Platform(platform_height=5, platform_width=5)

    @pytest.mark.parametrize(
        "x_axis, y_axis",
        [
            (1, 1),
            (2, 2),
            (4, 3),
        ],
    )
    def test_is_coordinate_available(
        self, robot_platform_fixture, x_axis, y_axis
    ):
        assert robot_platform_fixture.is_coordinate_available(
            x_axis=x_axis, y_axis=y_axis
        )

    @pytest.mark.parametrize(
        "x_axis, y_axis",
        [
            (-1, 1),
            (10, 10),
            (4, -3),
        ],
    )
    def test_is_coordinate_not_available(
        self, robot_platform_fixture, x_axis, y_axis
    ):
        assert not robot_platform_fixture.is_coordinate_available(
            x_axis=x_axis, y_axis=y_axis
        )
