import requests

# If running on same PC, use localhost. 
# If testing from another device, replace with your LAN IP (e.g., http://192.168.43.14:5000)
API_URL = "http://127.0.0.1:5000/predict"

# Example input
payload = {
    "memory_mib": 512
}

try:
    response = requests.post(API_URL, json=payload)

    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
except Exception as e:
    print("Error:", e)
