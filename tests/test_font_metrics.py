import pytest
import font_roboto

from design_units import DesignUnits
from font_metrics import MetricsFromFile, GlyphMetrics, MetricsPrecalculated
from fonts import Font


@pytest.fixture
def metrics(metrics_reads_file):
    return Font.metrics.glyph_metrics(font_roboto.RobotoBold, "y")


def test_glyph_width_in_units(metrics):
    assert metrics.width.units() == 1021


def test_glyph_width_in_em(metrics):
    assert metrics.width.to_em() == 0.49853515625


def test_glyph_width_in_points(metrics):
    assert metrics.width.to_points(font_size=16) == 7.9765625


def test_glyph_width_to_pixels(metrics):
    assert (metrics.width * 16).to_pixels() == 8


def test_y_max_pixels_are_rounded_points(metrics):
    points = metrics.y_max.to_points(16)
    pixels = (metrics.y_max * 16).to_pixels()
    assert pixels == round(points)


def test_width_is_xmin_xmax_difference(metrics):
    assert metrics.width == DesignUnits(1025 - 4, 2048)


def test_height_includes_above_and_below_baseline(metrics):
    assert metrics.height == DesignUnits(1082 + 437, 2048)


def test_should_raise_if_missing_glyph():
    with pytest.raises(KeyError):
        _ = Font.metrics.glyph_metrics(font_roboto.RobotoBold, " ")


def test_read_metrics_has_units_per_em():
    metrics = MetricsFromFile()
    assert metrics.units_per_em(font_roboto.RobotoBold) == 2048


def test_precalculated_units_per_em():
    from_file = MetricsFromFile().units_per_em(font_roboto.RobotoBold)
    precalculated = MetricsPrecalculated().units_per_em(font_roboto.RobotoBold)

    assert from_file == precalculated


@pytest.mark.parametrize(
    "char", ["S", "M", "T", "W", "F"]
)
def test_precalculated_glyph_metrics(char):
    metrics_from_file = MetricsFromFile().glyph_metrics(font_roboto.RobotoBold, char)
    metrics_precalculated = MetricsPrecalculated().glyph_metrics(font_roboto.RobotoBold, char)

    assert metrics_precalculated == metrics_from_file
