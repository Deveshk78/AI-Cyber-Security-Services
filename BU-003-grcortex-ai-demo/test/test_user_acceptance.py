from fastapi.testclient import TestClient

from monitoring.telemetry_engine import app


def test_user_acceptance_endpoint_returns_action_required_when_threshold_is_exceeded():
    client = TestClient(app)

    response = client.post(
        "/v1/grc/telemetry-hook",
        json={
            "asset_id": "mod_42",
            "drift_score": 0.18,
            "bias_disparity_index": 0.06,
            "hallucination_rate": 0.03,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["asset_id"] == "mod_42"
    assert payload["status"] == "ACTION_REQUIRED"
    assert any(item["control"] == "CTRL_DRIFT_01" for item in payload["flagged_controls"])
