import time

from monitoring.telemetry_engine import ModelTelemetry, evaluate_realtime_compliance


def test_performance_of_compliance_evaluation_remains_fast():
    start = time.perf_counter()

    for index in range(200):
        evaluate_realtime_compliance(
            ModelTelemetry(
                asset_id=f"perf_{index}",
                drift_score=0.12,
                bias_disparity_index=0.03,
                hallucination_rate=0.01,
            )
        )

    elapsed = time.perf_counter() - start

    assert elapsed < 1.0, f"Compliance evaluation took too long: {elapsed:.3f}s"
