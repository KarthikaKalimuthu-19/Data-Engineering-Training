import json

with open("products.json", "r") as f:
    data = json.load(f)

for item in data:
    item["price"] = round(item["price"] * 1.10, 2)

with open("products_updated.json", "w") as f:
    json.dump(data, f, indent=2)
