from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import os
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Gauge

# Initialize Flask and Prometheus
app = Flask(__name__)
metrics = PrometheusMetrics(app)

# ✅ Define a Prometheus metric for predicted CPU usage
predicted_cpu_metric = Gauge("predicted_cpu_mcores", "Predicted CPU usage in millicores")
input_memory_metric = Gauge("input_memory_mib", "Input memory value in MiB")

# ✅ Load model from /app/models (inside container)
model_path = os.path.join(os.path.dirname(__file__), "../models/best_model.pkl")
model = joblib.load(model_path)

# Home route
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Web UI prediction route
@app.route("/predict_web", methods=["POST"])
def predict_web():
    memory_mib = request.form.get("memory_mib")
    if memory_mib:
        memory_mib = float(memory_mib)
        input_df = pd.DataFrame([[memory_mib]], columns=["memory_mib"])
        prediction = model.predict(input_df)[0]

        # 🔥 Update Prometheus metrics
        input_memory_metric.set(memory_mib)
        predicted_cpu_metric.set(round(float(prediction), 2))

        return render_template("index.html", prediction=round(float(prediction), 2))
    return render_template("index.html", prediction="Error: Missing input")

# API prediction route (for JSON)
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    memory_mib = data.get("memory_mib")
    if memory_mib is None:
        return jsonify({"error": "Missing 'memory_mib' field"}), 400

    input_df = pd.DataFrame([[memory_mib]], columns=["memory_mib"])
    prediction = model.predict(input_df)[0]

    # 🔥 Update Prometheus metrics
    input_memory_metric.set(memory_mib)
    predicted_cpu_metric.set(round(float(prediction), 2))

    return jsonify({
        "memory_mib": memory_mib,
        "predicted_cpu_mcores": round(float(prediction), 2)
    })

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
