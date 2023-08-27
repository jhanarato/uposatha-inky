import pytest

from font_metrics import MetricsFromFile, MetricsPrecalculated
from fonts import Font


@pytest.fixture
def read_from_file():
    Font.metrics = MetricsFromFile()


@pytest.fixture
def precalculate():
    Font.metrics = MetricsPrecalculated()
