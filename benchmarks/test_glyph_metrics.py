from font_roboto import RobotoBold

from fonts import Font


def five_letter_metrics():
    for letter in "SMTWF":
        _ = Font.metrics.glyph_metrics(RobotoBold, letter)


def test_five_letters_read(benchmark, read_from_file):
    benchmark(five_letter_metrics)


def test_five_letters_precalculated(benchmark, precalculate):
    benchmark(five_letter_metrics)
