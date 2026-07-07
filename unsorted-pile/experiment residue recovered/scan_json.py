import json

# Path to your JSON
file_path = r"C:\Users\ANN\Hub\conversations.json"

# Load and scan
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Top level type: {type(data)}")
if isinstance(data, list):
    print(f"Total conversations: {len(data)}")
    if len(data) > 0:
        print("\nFirst conversation keys:")
        print(list(data[0].keys()))
elif isinstance(data, dict):
    print(f"Top level keys: {list(data.keys())}")
else:
    print("Unknown structure.")

# Optionally print first entry preview (short version)
print("\nFirst item preview:")
print(json.dumps(data[0] if isinstance(data, list) else data, indent=2)[:1000])