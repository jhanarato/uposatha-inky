import pytest
import font_roboto

from design_units import DesignUnits
from glyph_metrics import glyph_metrics


@pytest.fixture
def metrics():
    return glyph_metrics(font_roboto.RobotoBold, "y")


def test_glyph_width_in_units(metrics):
    assert metrics.width.units() == 1021


def test_glyph_width_in_em(metrics):
    assert metrics.width.to_em() == 0.49853515625


def test_glyph_width_in_points(metrics):
    assert metrics.width.to_points(font_size=16) == 7.9765625


def test_glyph_width_to_pixels(metrics):
    assert metrics.width.to_pixels(font_points_per_em=16) == 8


def test_width_is_xmin_xmax_difference(metrics):
    assert metrics.width == DesignUnits(1025 - 4, 2048)


def test_height_includes_above_and_below_baseline(metrics):
    assert metrics.height == DesignUnits(1082 + 437, 2048)


def test_should_raise_if_missing_glyph():
    with pytest.raises(KeyError):
        _ = glyph_metrics(font_roboto.RobotoBold, " ")
