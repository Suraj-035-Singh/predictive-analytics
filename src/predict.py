import os
import joblib
import numpy as np

# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/best_model.pkl")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"❌ Trained model not found at {MODEL_PATH}. Run train_model.py first.")

model = joblib.load(MODEL_PATH)
print("✅ Model loaded successfully!")

# Example prediction
def predict_cpu(memory_value):
    prediction = model.predict(np.array([[memory_value]]))[0]
    return round(prediction, 2)

# Test
memory_input = 512  # MiB
pred = predict_cpu(memory_input)
print(f"📊 Predicted CPU usage for {memory_input} MiB memory: {pred} mcores")
