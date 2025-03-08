import requests

API_URL = "http://127.0.0.1:5000/predict"

# Test input data
test_data = {
    "Temperature": 30,
    "RH": 40,
    "Ws": 10,
    "Rain": 0,
    "FFMC": 85.1,
    "DMC": 110.2,
    "DC": 500,
    "ISI": 9.2,
    "BUI": 60.4,
    "FWI": 10.5
}

# Send request to API
response = requests.post(API_URL, json=test_data)

# Check if request was successful
if response.status_code == 200:
    response_json = response.json()
    
    # Debug: Print full API response
    print("\n✅ API Response:")
    print(response_json)
    
    # Extract severity information
    if "severity" in response_json:
        print(f"\n🔥 Fire Severity Level: {response_json['severity']}\n")
        print(f"📢 {response_json['message']}\n")
        print(f"🌍 Real-World Impact: {response_json['impact']}\n")
        print("🛠️ Precautionary Measures:")
        for i, precaution in enumerate(response_json["precautions"], 1):
            print(f"  {i}. {precaution}")
    else:
        print("\n❌ 'severity' key is missing. Check app.py!\n")
else:
    print(f"\n❌ API Error: {response.status_code} - {response.text}\n")
