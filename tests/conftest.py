import pytest

from font_metrics import MetricsFromFile, MetricsPrecalculated
from fonts import Font


@pytest.fixture
def metrics_reads_file():
    current = Font.metrics
    Font.metrics = MetricsFromFile()
    yield
    Font.metrics = current


@pytest.fixture
def metrics_precalculates():
    current = Font.metrics
    Font.metrics = MetricsPrecalculated()
    yield
    Font.metrics = current
