import requests

url = "http://127.0.0.1:8000/v1/grc/telemetry-hook"
payload = {
    "asset_id": "mod_01",
    "drift_score": 0.18,  # Triggers breach (> 0.15)
    "bias_disparity_index": 0.02,
    "hallucination_rate": 0.01
}

response = requests.post(url, json=payload)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())