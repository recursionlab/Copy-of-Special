import json
from pathlib import Path

# Load filtered seeds
with open('filtered_seeds.json', 'r', encoding='utf-8') as f:
    filtered_clusters = json.load(f)

output_folder = Path("loadouts")
output_folder.mkdir(exist_ok=True)

count = 0

for topic, seeds in filtered_clusters.items():
    loadout = {
        "topic": topic,
        "seed_count": len(seeds),
        "seeds": seeds
    }
    path = output_folder / f"loadout_{topic.lower()}.json"
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(loadout, f, indent=2, ensure_ascii=False)
    print(f"✅ Loadout created: {path.name} ({len(seeds)} seeds)")
    count += 1

print(f"🏁 {count} loadouts forged into /loadouts/")
