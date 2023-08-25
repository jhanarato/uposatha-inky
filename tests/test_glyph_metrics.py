import pytest
import font_roboto

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


def test_width_is_xmin_xmax_difference(metrics):
    difference = metrics.x_max - metrics.x_min
    assert metrics.width == difference


def test_should_raise_if_missing_glyph():
    with pytest.raises(KeyError):
        _ = glyph_metrics(font_roboto.RobotoBold, " ")
