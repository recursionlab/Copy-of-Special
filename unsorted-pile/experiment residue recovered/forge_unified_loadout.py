import json
import os

# Path to your loadouts folder
loadout_folder = "loadouts"

# Unified seeds container
unified_seeds = []

# Process each loadout file
for filename in os.listdir(loadout_folder):
    if filename.endswith(".json"):
        with open(os.path.join(loadout_folder, filename), "r", encoding="utf-8") as f:
            data = json.load(f)
            seeds = data.get("seeds", [])
            unified_seeds.extend(seeds)

# Optional: De-duplicate seeds by (node_id)
seen_ids = set()
unique_seeds = []
for seed in unified_seeds:
    node_id = seed.get("node_id")
    if node_id and node_id not in seen_ids:
        seen_ids.add(node_id)
        unique_seeds.append(seed)

# Save the unified loadout
with open("unified_loadout.json", "w", encoding="utf-8") as f:
    json.dump(unique_seeds, f, ensure_ascii=False, indent=2)

print(f"✅ Unified loadout saved ➔ unified_loadout.json with {len(unique_seeds)} unique seeds.")