from monitoring.telemetry_engine import ModelTelemetry, evaluate_realtime_compliance


def test_stress_simulation_handles_many_requests_without_failure():
    for index in range(250):
        response = evaluate_realtime_compliance(
            ModelTelemetry(
                asset_id=f"stress_{index}",
                drift_score=0.05 if index % 2 == 0 else 0.18,
                bias_disparity_index=0.02 if index % 3 == 0 else 0.06,
                hallucination_rate=0.01,
            )
        )

        assert response["asset_id"] == f"stress_{index}"
        assert response["status"] in {"COMPLIANT", "ACTION_REQUIRED"}
        assert isinstance(response["flagged_controls"], list)
