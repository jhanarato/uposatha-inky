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


def test_glyph_left_side_bearing(metrics):
    assert metrics.left_side_bearing.units() == 130


def test_lsb_as_points(metrics):
    assert metrics.left_side_bearing.to_points(font_size=30) == 1.904296875


def test_width_is_xmin_xmax_difference(metrics):
    difference = metrics.x_max.units() - metrics.x_min.units()
    assert metrics.glyph_width.units() == difference


def test_lsb_is_xmin(metrics):
    assert metrics.left_side_bearing.units() == metrics.x_min.units()


def test_should_raise_if_missing_glyph():
    with pytest.raises(KeyError):
        _ = glyph_metrics(font_roboto.RobotoBold, " ")
