import json
from collections import defaultdict

# Load seeds
with open('extracted_seeds.json', 'r', encoding='utf-8') as f:
    seeds = json.load(f)

# Cluster by simple heuristics: by conversation title keyword
clusters = defaultdict(list)

for seed in seeds:
    title = seed.get('conversation_title', 'Misc')
    topic = title.split()[0] if title else 'Misc'
    clusters[topic].append(seed)

# Save clustered seeds
with open('clustered_seeds.json', 'w', encoding='utf-8') as f:
    json.dump(clusters, f, indent=2, ensure_ascii=False)

print(f"✅ Clustered {len(seeds)} seeds into {len(clusters)} topic groups ➔ clustered_seeds.json")
