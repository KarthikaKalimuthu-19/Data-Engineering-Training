import json

with open('data.json', 'r') as f:
    data = json.load(f)

print("JSON Read:\n", data)

with open('output.json', 'w') as f:
    json.dump(data, f, indent=4)

print("JSON written to output.json")