import pytest

from models.platform import Platform


class TestPlatform:

    @pytest.mark.parametrize(
        "x_axis, y_axis",
        [
            (1, 1),
            (2, 2),
            (4, 3),
        ],
    )
    def test_is__coordinate__not_available(self, x_axis, y_axis):
        platform = Platform(platform_height=5, platform_width=5)
        assert platform.is_coordinate_available(x_axis=x_axis, y_axis=y_axis)

    @pytest.mark.parametrize(
        "x_axis, y_axis",
        [
            (-1, 1),
            (10, 10),
            (4, -3),
        ],
    )
    def test_is_coordinate_available(self, x_axis, y_axis):
        platform = Platform(platform_height=5, platform_width=5)
        assert not platform.is_coordinate_available(x_axis=x_axis, y_axis=y_axis)
