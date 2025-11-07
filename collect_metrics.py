import subprocess
import time
import csv
from datetime import datetime

# File to save metrics
CSV_FILE = "metrics.csv"

# Interval in seconds (e.g., 10 sec)
INTERVAL = 10

# Write CSV header if file is empty
with open(CSV_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "pod", "cpu_mcores", "memory_mib"])

print("📊 Collecting pod metrics... (Press Ctrl+C to stop)")

try:
    while True:
        # Run kubectl top pods command
        result = subprocess.run(
            ["kubectl", "top", "pods", "--no-headers"],
            capture_output=True, text=True
        )

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Parse output and write to CSV
        with open(CSV_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            for line in result.stdout.strip().split("\n"):
                if not line.strip():
                    continue
                parts = line.split()
                pod = parts[0]
                cpu = parts[1].replace("m", "")  # CPU in millicores
                memory = parts[2].replace("Mi", "")  # Memory in MiB
                writer.writerow([now, pod, cpu, memory])

        print(f"[{now}] ✅ Metrics collected.")

        time.sleep(INTERVAL)

except KeyboardInterrupt:
    print("\n⏹️ Stopped metrics collection.")
