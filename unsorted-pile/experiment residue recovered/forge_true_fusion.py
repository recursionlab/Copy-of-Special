import json
import difflib
import os

# Load filtered seeds
with open("filtered_seeds.json", "r", encoding="utf-8") as f:
    clusters = json.load(f)

# Flatten all seeds
all_seeds = []
for cluster in clusters:
    all_seeds.extend(cluster["seeds"])

print(f"🔵 Loaded {len(all_seeds)} seeds before fusion.")

# Normalize seeds (trim whitespace, lowercase for comparison)
normalized_seeds = []
for seed in all_seeds:
    text = seed["text"].strip().lower()
    normalized_seeds.append((text, seed))

# Deduplicate seeds
fused_seeds = []
seen_texts = set()

for text, seed in normalized_seeds:
    if text not in seen_texts:
        fused_seeds.append(seed)
        seen_texts.add(text)

print(f"🧩 After exact deduplication: {len(fused_seeds)} seeds.")

# Optional: Soft merge for *near-duplicates*
# We'll treat anything >90% similarity as a duplicate
final_seeds = []
soft_seen = set()

for i, seed1 in enumerate(fused_seeds):
    if i in soft_seen:
        continue
    text1 = seed1["text"]
    group = [seed1]

    for j in range(i + 1, len(fused_seeds)):
        if j in soft_seen:
            continue
        text2 = fused_seeds[j]["text"]
        similarity = difflib.SequenceMatcher(None, text1, text2).ratio()
        if similarity > 0.90:
            group.append(fused_seeds[j])
            soft_seen.add(j)

    # Merge if needed: here, just keep the first
    final_seeds.append(group[0])

print(f"⚡ Final unified seeds: {len(final_seeds)}.")

# Save
unified_output = {
    "total_seeds": len(final_seeds),
    "seeds": final_seeds
}

os.makedirs("loadouts", exist_ok=True)
with open("loadouts/unified_prime_loadout.json", "w", encoding="utf-8") as f:
    json.dump(unified_output, f, indent=2, ensure_ascii=False)

print("✅ True Fusion Complete ➔ Saved to loadouts/unified_prime_loadout.json")
