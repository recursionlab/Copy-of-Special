import json

with open("loadouts/loadout_prime-wave.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(type(data))
print(list(data.keys()))  # <--- show the keys