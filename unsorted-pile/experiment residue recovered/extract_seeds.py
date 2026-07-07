import json
import os

# CONFIG
input_file = "conversations.json"
output_file = "extracted_seeds.json"
top_convos = [82, 341, 31, 129, 80]  # Your Top 5
critical_threshold = 500  # chars to qualify as "Critical-Seed"

def extract_seeds():
    if not os.path.exists(input_file):
        print(f"❌ Cannot find {input_file}")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    seeds = []

    for idx in top_convos:
        convo = data[idx]
        title = convo.get("title", f"Conversation {idx}")
        mapping = convo.get("mapping", {})

        for node_id, node in mapping.items():
            msg = node.get("message")
            if not msg or not isinstance(msg, dict):
                continue

            content = msg.get("content", {})
            parts = content.get("parts", [])
            if not parts:
                continue

            for part in parts:
                if isinstance(part, str) and part.strip():
                    tag = "Critical-Seed" if len(part.strip()) >= critical_threshold else "Support-Seed"
                    seeds.append({
                        "conversation_index": idx,
                        "conversation_title": title,
                        "node_id": node_id,
                        "seed_type": tag,
                        "text": part.strip()
                    })

    with open(output_file, "w", encoding="utf-8") as out:
        json.dump(seeds, out, indent=2, ensure_ascii=False)

    print(f"✅ Seed Extraction Complete. Saved {len(seeds)} seeds ➔ {output_file}")

if __name__ == "__main__":
    extract_seeds()
