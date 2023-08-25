import pytest
import font_roboto

from glyph_metrics import glyph_metrics


@pytest.fixture
def metrics():
    return glyph_metrics(font_roboto.RobotoBold, "H")


def test_glyph_width_in_units(metrics):
    assert metrics.glyph_width.units() == 1186


def test_glyph_width_in_em(metrics):
    assert metrics.glyph_width.to_em() == 0.5791015625


def test_glyph_width_in_points(metrics):
    assert metrics.glyph_width.to_points(font_size=16) == 9.265625


def test_width_is_xmin_xmax_difference(metrics):
    difference = metrics.x_max - metrics.x_min
    assert metrics.glyph_width == difference


def test_should_raise_if_missing_glyph():
    with pytest.raises(KeyError):
        _ = glyph_metrics(font_roboto.RobotoBold, " ")
