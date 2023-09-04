import pytest

from font_roboto import RobotoBold

from fonts import fonts, Font
from design_units import DesignUnits


def test_font_dictionary():
    for _, path in fonts.items():
        assert path[-4:] == ".ttf"


@pytest.fixture
def font():
    return Font("roboto-bold", size=30)


def test_should_have_family(font):
    assert font.family == "Roboto"


def test_should_have_style(font):
    assert font.style == "Bold"


def test_should_have_ascent(font):
    assert font.ascent() == 28


def test_should_have_descent(font):
    assert font.descent().to_pixels() == 8


def test_should_measure_height_of_text(font):
    assert font.height("Hello") == 28


def test_should_measure_width_of_text(font):
    assert font.width("Hello") == 70


def test_should_raise_if_font_unavailable():
    with pytest.raises(KeyError):
        _ = Font("Not-a-font", 100)


@pytest.fixture
def units():
    return DesignUnits(units=100, units_per_em=2000)


def test_design_units_available(units):
    assert units.units() == 100


def test_design_units_converts_to_em(units):
    assert units.to_em() == 0.05


def test_design_converts_font_points_to_glyph_points(units):
    assert units.to_points(font_size=10) == 0.5


def test_font_class_provides_metrics():
    assert Font.metrics.units_per_em(RobotoBold) == 2048
