import requests
import json
from pathlib import Path

label_id = 82118

url = f"https://api.ods.od.nih.gov/dsld/v9/label/{label_id}"

response = requests.get(url, timeout = 30)
print(response.status_code)

response.raise_for_status()

label_data = response.json()

print(type(label_data))
print(label_data["id"])

output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

output_path = output_dir / f"label_{label_id}_my_version.json"

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(label_data, f, indent=4)