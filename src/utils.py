import pandas as pd
import os

def load_data():
    data_path = os.path.join(os.path.dirname(__file__), "../data/metrics.csv")
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"❌ Dataset not found at {data_path}")
    
    df = pd.read_csv(data_path)
    print(f"✅ Data loaded successfully! Shape: {df.shape}")
    return df
