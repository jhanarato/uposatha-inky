import pytest

from fonts import glyph_centered_x
from fonts import Font, DesignUnits, GlyphMetrics
from bbox import BBox


@pytest.fixture
def font():
    return Font(size=30)


def test_should_have_family(font):
    assert font.family == "Roboto"


def test_should_have_style(font):
    assert font.style == "Bold"


def test_should_measure_height_of_text(font):
    assert font.height("Hello") == 28


def test_should_measure_width_of_text(font):
    assert font.width("Hello") == 70


def test_should_raise_if_missing_glyph(font):
    with pytest.raises(KeyError):
        _ = font.glyph_metrics(" ")


@pytest.fixture
def metrics(font):
    return font.glyph_metrics("H")


def test_glyph_width_in_units(metrics):
    assert metrics.glyph_width.units() == 1448


def test_glyph_width_in_em(metrics):
    assert metrics.glyph_width.to_em() == 0.70703125


def test_glyph_width_in_points(metrics):
    assert metrics.glyph_width.to_points(font_size=16) == 11.3125


def test_glyph_left_side_bearing(metrics):
    assert metrics.left_side_bearing.units() == 130


def test_lsb_as_points(metrics):
    assert metrics.left_side_bearing.to_points(font_size=30) == 1.904296875


@pytest.fixture
def units():
    return DesignUnits(units=100, units_per_em=2000)


def test_design_units_available(units):
    assert units.units() == 100


def test_design_units_converts_to_em(units):
    assert units.to_em() == 0.05


def test_design_converts_font_points_to_glyph_points(units):
    assert units.to_points(font_size=10) == 0.5


def test_should_center_glyph_horizontally():
    bbox = BBox(left=10, right=60, top=20, bottom=40)

    assert bbox.center[0] == 35

    metrics = GlyphMetrics(
        glyph_width=DesignUnits(800, 1000),        # 8 points for 10 point font
        left_side_bearing=DesignUnits(200, 1000),  # 2 points for 10 point font
        x_min=DesignUnits(0, 0),
        x_max=DesignUnits(0, 0),
        y_min=DesignUnits(0, 0),
        y_max=DesignUnits(0, 0),
    )

    assert glyph_centered_x(bbox, metrics, font_points=10) == 29
