from design_units import DesignUnits


def test_design_units_are_equal():
    assert DesignUnits(100, 1000) == DesignUnits(100, 1000)


def test_design_units_are_not_equal():
    assert DesignUnits(100, 1000) != DesignUnits(101, 1000)


def test_units_per_em_are_not_equal():
    assert DesignUnits(100, 1000) != DesignUnits(100, 1001)


def test_units_compared_to_non_units():
    assert DesignUnits(100, 1000) != 100


def test_subtract_units():
    assert DesignUnits(100, 1000) - DesignUnits(75, 1000) == DesignUnits(25, 1000)


def test_add_units():
    assert DesignUnits(25, 1000) + DesignUnits(75, 1000) == DesignUnits(100, 1000)


def test_multipy_units():
    assert DesignUnits(11, 1000) * 9 == DesignUnits(99, 1000)


def test_round_units_multiplication():
    assert DesignUnits(1, 1000) * 1.1 == DesignUnits(1, 1000)


def test_from_points():
    assert DesignUnits.from_points(8, 1000) == DesignUnits(8000, 1000)
