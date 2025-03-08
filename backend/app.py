from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load trained model and scaler
kmeans = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Feature names (must match training dataset)
feature_names = ["Temperature", "RH", "Ws", "Rain", "FFMC", "DMC", "DC", "ISI", "BUI", "FWI"]

# Severity Levels
severity_levels = {
    0: {"severity": "Low", "message": "Your forest is safe. Probability of fire occurring is 0.00%.",
        "impact": "Even if a fire starts, it may not spread.",
        "precautions": ["Monitor weather conditions.", "Maintain fire breaks.", "Ensure fire safety equipment."]},
    1: {"severity": "Medium", "message": "Moderate fire risk. Stay alert.",
        "impact": "Fire can spread but is manageable.",
        "precautions": ["Keep firefighting tools ready.", "Avoid campfires.", "Educate local communities."]},
    2: {"severity": "High", "message": "Extreme fire risk! Immediate precautions required.",
        "impact": "Fire will spread rapidly and be difficult to control.",
        "precautions": ["Evacuate high-risk areas.", "Keep emergency contacts ready.", "Avoid ignition sources."]}
}

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Validate input features
        missing_features = [feature for feature in feature_names if feature not in data]
        if missing_features:
            return jsonify({"error": f"Missing input features: {missing_features}"}), 400

        # Convert input to DataFrame
        input_df = pd.DataFrame([data], columns=feature_names)

        # Scale input data
        input_scaled = scaler.transform(input_df)

        # Predict cluster (severity level)
        cluster = kmeans.predict(input_scaled)[0]

        # Validate and get severity response
        severity_response = severity_levels.get(cluster, {
            "severity": "Unknown",
            "message": "Unable to determine fire risk.",
            "impact": "No data available.",
            "precautions": ["Consult local authorities for fire safety."]
        })

        return jsonify(severity_response)

    except Exception as e:
        return jsonify({"error": str(e), "severity": "Unknown"}), 500

if __name__ == "__main__":
    app.run(debug=True)
