import pytest

from fontTools.ttLib import TTFont
from font_roboto import RobotoBold

from fonts import glyph_centered_x, extract_metrics
from fonts import Font, DesignUnits, Glyph, GlyphMetrics
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


@pytest.fixture
def glyph():
    font = TTFont(RobotoBold)
    return Glyph(font, "H")


def test_glyph_width_in_units(glyph):
    assert glyph.metrics().glyph_width.units() == 1448


def test_glyph_width_in_em(glyph):
    assert glyph.metrics().glyph_width.to_em() == 0.70703125


def test_glyph_width_in_points(glyph):
    assert glyph.metrics().glyph_width.to_points(font_size=16) == 11.3125


def test_glyph_left_side_bearing(glyph):
    assert glyph.metrics().left_side_bearing.units() == 130


def test_lsb_as_points(glyph):
    assert glyph.metrics().left_side_bearing.to_points(font_size=30) == 1.904296875


def test_design_units_available():
    units = DesignUnits(units=100, units_per_em=2000)
    assert units.units() == 100


def test_design_units_converts_to_em():
    units = DesignUnits(units=100, units_per_em=2000)
    assert units.to_em() == 0.05


def test_design_converts_font_points_to_glyph_points():
    units = DesignUnits(units=100, units_per_em=2000)
    assert units.to_points(font_size=10) == 0.5


def test_glyph_with_space():
    glyph = Glyph(TTFont(RobotoBold), " ")
    with pytest.raises(KeyError):
        _ = glyph.metrics()


def test_should_center_glyph_horizontally():
    bbox = BBox(left=10, right=60, top=20, bottom=40)

    assert bbox.center[0] == 35

    metrics = GlyphMetrics(
        glyph_width=DesignUnits(800, 1000),        # 8 points for 10 point font
        left_side_bearing=DesignUnits(200, 1000),  # 2 points for 10 point font
    )

    assert glyph_centered_x(bbox, metrics, font_points=10) == 29


def test_should_convert_glyph_metrics():
    glyphtools_dict = {"width": 100, "lsb": 200}
    metrics = extract_metrics(glyphtools_dict, 0)
    assert metrics.glyph_width.units() == 100


def test_should_provide_fonttools_object(font):
    assert isinstance(font.as_fonttools(), TTFont)


def test_should_provide_glyph_metrics(font):
    assert font.glyph_metrics("H").glyph_width.units() == 1448
