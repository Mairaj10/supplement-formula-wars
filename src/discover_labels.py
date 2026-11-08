import requests
import json
from pathlib import Path

url = "https://api.ods.od.nih.gov/dsld/v9/browse-products/"

params = {
    "method": "by_keyword",
    "q": "Creatine",
    "size": 5,
    "from": 0
}

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()  # Raise an exception for HTTP errors

search_data = response.json()

output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

for hit in search_data["hits"]:
    label_id = hit["_id"]
    print(label_id)

    detail_url = f"https://api.ods.od.nih.gov/dsld/v9/label/{label_id}"

    response= requests.get(detail_url, timeout=30)
    response.raise_for_status()  # Raise an exception for HTTP errors
    label_data = response.json()

    if str(label_data["id"]) != str(label_id):
        raise ValueError("Downloaded label ID does not match the requested ID")

    output_path = output_dir / f"label_{label_id}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(label_data, f, indent=4)


    print(f"Saved {output_path}")

    