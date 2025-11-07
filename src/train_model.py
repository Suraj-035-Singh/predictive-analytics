import os
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from utils import load_data

# Load data
df = load_data()

# Features & target
X = df[["memory_mib"]]
y = df["cpu_mcores"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Models
models = {
    "LinearRegression": LinearRegression(),
    "RandomForest": RandomForestRegressor(random_state=42),
    "XGBoost": XGBRegressor(objective="reg:squarederror", random_state=42)
}

results = {}
best_model_name, best_score, best_model = None, -9999, None

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    results[name] = {"R2": r2, "MAE": mae, "RMSE": rmse}

    print(f"\n📌 {name} Results:")
    print(f"   R² Score : {r2:.4f}")
    print(f"   MAE      : {mae:.4f}")
    print(f"   RMSE     : {rmse:.4f}")

    if r2 > best_score:
        best_score = r2
        best_model_name = name
        best_model = model

# Save best model
MODEL_DIR = os.path.join(os.path.dirname(__file__), "../models")
os.makedirs(MODEL_DIR, exist_ok=True)

model_path = os.path.join(MODEL_DIR, "best_model.pkl")
joblib.dump(best_model, model_path)

print(f"\n✅ Best model is {best_model_name} with R² = {best_score:.4f}")
print(f"✅ Model saved at: {model_path}")
