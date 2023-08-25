from typing import Self


class DesignUnits:
    def __init__(self, units: int, units_per_em: int):
        self._units = units
        self._units_per_em = units_per_em

    def units(self) -> int:
        return self._units

    def to_em(self) -> float:
        return self.units() / self._units_per_em

    def to_points(self, font_size: int) -> float:
        return self.to_em() * font_size

    def to_pixels(self, font_points_per_em: int) -> int:
        return round(self.to_em() * font_points_per_em)

    def __eq__(self, other):
        if not isinstance(other, DesignUnits):
            return NotImplemented

        units_eq = self._units == other._units
        units_per_em_eq = self._units_per_em == other._units_per_em
        return units_eq and units_per_em_eq

    def __sub__(self, other):
        if not isinstance(other, DesignUnits):
            return NotImplemented

        if not self._units_per_em == self._units_per_em:
            return NotImplemented

        units = self._units - other._units
        return DesignUnits(units, self._units_per_em)

    def __add__(self, other):
        if not isinstance(other, DesignUnits):
            return NotImplemented

        if not self._units_per_em == self._units_per_em:
            return NotImplemented

        units = self._units + other._units
        return DesignUnits(units, self._units_per_em)

    def __mul__(self, multiplicand: float) -> Self:
        if not self._units_per_em == self._units_per_em:
            return NotImplemented

        try:
            scale_by = float(multiplicand)
        except TypeError:
            return NotImplemented

        units = round(self._units * scale_by)
        return DesignUnits(units, self._units_per_em)
