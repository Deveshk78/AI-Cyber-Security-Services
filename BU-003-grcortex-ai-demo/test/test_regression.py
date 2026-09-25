from monitoring.telemetry_engine import ModelTelemetry, evaluate_realtime_compliance


def test_realtime_compliance_regression_for_compliant_payload():
    response = evaluate_realtime_compliance(
        ModelTelemetry(
            asset_id="mod_104",
            drift_score=0.10,
            bias_disparity_index=0.03,
            hallucination_rate=0.01,
        )
    )

    assert response["asset_id"] == "mod_104"
    assert response["status"] == "COMPLIANT"
    assert response["flagged_controls"] == []


def test_realtime_compliance_regression_for_action_required_payload():
    response = evaluate_realtime_compliance(
        ModelTelemetry(
            asset_id="mod_200",
            drift_score=0.20,
            bias_disparity_index=0.01,
            hallucination_rate=0.00,
        )
    )

    assert response["status"] == "ACTION_REQUIRED"
    assert any(item["control"] == "CTRL_DRIFT_01" for item in response["flagged_controls"])
