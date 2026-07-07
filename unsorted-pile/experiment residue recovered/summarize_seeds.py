import json
from collections import Counter

# Load seeds
with open('extracted_seeds.json', 'r', encoding='utf-8') as f:
    seeds = json.load(f)

# Count seed types by basic shape
counter = Counter()
for seed in seeds:
    if isinstance(seed, dict):
        key = tuple(sorted(seed.keys()))
        counter[key] += 1
    else:
        counter[type(seed).__name__] += 1

# Show top seeds
print(f"✅ Loaded {len(seeds)} seeds.")
print("Top seed structures:")
for structure, count in counter.most_common(20):
    print(f"• {structure}: {count}")

# Save summary
summary = {
    "total_seeds": len(seeds),
    "top_structures": counter.most_common(50)
}
with open('seeds_summary.json', 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2)

print("✅ Seeds summary saved ➔ seeds_summary.json")
