import json
import os

file_path = "conversations.json"  # Update if needed

# === Deep Scan Config ===
max_preview_length = 120  # Max chars to preview
max_safe_children = 20    # Flag trees with too many branches
large_message_threshold = 5000  # Characters
empty_message_flag = True
deep_debug = False  # Set True if you want full dump on weirdness

# === Deep Scanner ===
def deep_scan():
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"Deep scanning {len(data)} conversations...")

    issues = []

    for idx, convo in enumerate(data):
        mapping = convo.get("mapping", {})
        for node_id, node in mapping.items():
            msg = node.get("message")
            if msg:
                content = msg.get("content", {})
                parts = content.get("parts", [])
                if not parts:
                    issues.append((idx, node_id, "⚠️ Empty parts array"))
                elif any(isinstance(p, str) and p.strip() == "" for p in parts):
                    issues.append((idx, node_id, "⚠️ Empty string in parts"))
                elif any(len(p) > large_message_threshold for p in parts):
                    issues.append((idx, node_id, "⚠️ Large message"))
            else:
                if empty_message_flag:
                    issues.append((idx, node_id, "⚠️ Null message"))

            # Check node structure
            children = node.get("children", [])
            if children and len(children) > max_safe_children:
                issues.append((idx, node_id, f"⚠️ Excessive children: {len(children)}"))

    # === Output results ===
    print(f"\n✅ Deep Scan Finished. Found {len(issues)} issues.\n")

    if issues:
        for (convo_idx, node_id, issue) in issues[:100]:  # Cap output
            title = data[convo_idx].get("title", "Untitled")
            print(f"[Convo {convo_idx} | {title[:40]}...] Node {node_id[:8]}: {issue}")
    else:
        print("No anomalies detected.")

if __name__ == "__main__":
    deep_scan()