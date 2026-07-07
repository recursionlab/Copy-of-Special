import json

# Load clustered seeds
with open('clustered_seeds.json', 'r', encoding='utf-8') as f:
    clusters = json.load(f)

# Filter criteria: remove seeds that are too tiny or almost empty
MIN_TEXT_LENGTH = 40

filtered_clusters = {}

for topic, seeds in clusters.items():
    filtered = [s for s in seeds if s.get('text') and len(s['text']) >= MIN_TEXT_LENGTH]
    if filtered:
        filtered_clusters[topic] = filtered

# Save filtered seeds
with open('filtered_seeds.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_clusters, f, indent=2, ensure_ascii=False)

print(f"✅ Filtered clusters saved ➔ filtered_seeds.json")