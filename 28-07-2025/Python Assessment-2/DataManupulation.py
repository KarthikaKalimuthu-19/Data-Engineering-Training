import json

with open('inventory.json') as f:
    data = json.load(f)

for item in data:
    item['status'] = 'In Stock' if item['stock'] > 0 else 'Out of Stock'

with open('inventory_updated.json', 'w') as f:
    json.dump(data, f, indent=2)
