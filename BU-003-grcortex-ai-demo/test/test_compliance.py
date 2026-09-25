from monitoring.telemetry_engine import ModelTelemetry, evaluate_realtime_compliance


def test_threshold_boundary_values_are_compliant():
    response = evaluate_realtime_compliance(
        ModelTelemetry(
            asset_id="boundary_ok",
            drift_score=0.15,
            bias_disparity_index=0.05,
            hallucination_rate=0.02,
        )
    )

    assert response["status"] == "COMPLIANT"
    assert response["flagged_controls"] == []


def test_threshold_exceedance_triggers_action():
    response = evaluate_realtime_compliance(
        ModelTelemetry(
            asset_id="boundary_fail",
            drift_score=0.16,
            bias_disparity_index=0.05,
            hallucination_rate=0.02,
        )
    )

    assert response["status"] == "ACTION_REQUIRED"
    assert any(item["control"] == "CTRL_DRIFT_01" for item in response["flagged_controls"])
