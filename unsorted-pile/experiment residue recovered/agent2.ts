import json
import os

INPUT_PATH = "your_huge_export.json"
OUTPUT_DIR = "gpt_chunks"
CHUNK_SIZE = 50  # number of messages per chunk

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# Flatten messages in order
def extract_ordered_messages(data):
    mapping = data["mapping"]
    messages = []

    def traverse(node_id):
        node = mapping[node_id]
        msg = node.get("message")
        if msg and msg.get("content"):
            role = msg["author"]["role"]
            parts = msg["content"].get("parts", [])
            content = "\n".join(parts)
            messages.append({"role": role, "content": content})
        for child_id in node.get("children", []):
            traverse(child_id)

    root = [k for k, v in mapping.items() if v.get("parent") is None][0]
    traverse(root)
    return messages

messages = extract_ordered_messages(data)

# Split into chunks
for i in range(0, len(messages), CHUNK_SIZE):
    chunk = messages[i:i + CHUNK_SIZE]
    chunk_path = os.path.join(OUTPUT_DIR, f"chunk_{i // CHUNK_SIZE + 1}.json")
    with open(chunk_path, "w", encoding="utf-8") as f:
        json.dump(chunk, f, indent=2, ensure_ascii=False)

print(f"✅ Done! {len(messages) // CHUNK_SIZE + 1} chunks saved to '{OUTPUT_DIR}/'")