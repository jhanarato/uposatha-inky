import pytest

from font_metrics import MetricsFromFile, MetricsPrecalculated
from fonts import Font


@pytest.fixture
def read_from_file():
    current = Font.metrics
    Font.metrics = MetricsFromFile()
    yield
    Font.metrics = current


@pytest.fixture
def precalculate():
    current = Font.metrics
    Font.metrics = MetricsPrecalculated()
    yield
    Font.metrics = current
