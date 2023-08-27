from font_roboto import RobotoBold
from fonts import Font


def test_five_letter_metrics(benchmark):
    # This is the maximum that needs to be done for each run.
    def five_letter_metrics():
        for letter in "SMTWF":
            _ = Font.metrics.glyph_metrics(RobotoBold, letter)

    benchmark(five_letter_metrics)
