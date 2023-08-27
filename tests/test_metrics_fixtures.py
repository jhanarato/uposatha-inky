from font_metrics import MetricsFromFile, MetricsPrecalculated
from fonts import Font


def test_1_default_metrics():
    Font.metrics = MetricsFromFile()
    assert isinstance(Font.metrics, MetricsFromFile)


def test_2_metrics_changed_by_fixture(metrics_precalculates):
    assert isinstance(Font.metrics, MetricsPrecalculated)


def test_3_metrics_is_as_before_fixture():
    assert isinstance(Font.metrics, MetricsFromFile)


def test_4_set_to_precalculate():
    Font.metrics = MetricsPrecalculated()


def test_5_metrics_changed_by_fixture(metrics_reads_file):
    assert isinstance(Font.metrics, MetricsFromFile)


def test_6_metrics_return_to_precalculated():
    assert isinstance(Font.metrics, MetricsPrecalculated)
