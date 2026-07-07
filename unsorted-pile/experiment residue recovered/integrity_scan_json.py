import json
from collections import defaultdict

file_path = "conversations.json"

def integrity_scan():
    with open(file_path, "r", encoding="utf-8") as f:
        conversations = json.load(f)

    broken_links = []
    orphan_nodes = []
    parentless_roots = []

    for i, convo in enumerate(conversations):
        mapping = convo.get("mapping", {})
        seen_ids = set(mapping.keys())

        for node_id, node_data in mapping.items():
            parent = node_data.get("parent")
            children = node_data.get("children", [])

            # Check parent
            if parent and parent not in seen_ids:
                broken_links.append((i, node_id, "parent", parent))

            # Check children
            for child in children:
                if child not in seen_ids:
                    broken_links.append((i, node_id, "child", child))

        # Check for roots without message
        roots = [n for n in mapping.values() if n.get("parent") is None]
        if not any(r.get("message") for r in roots):
            parentless_roots.append(i)

    print(f"✅ Integrity scan complete.\n")
    print(f"Broken links found: {len(broken_links)}")
    print(f"Conversations with no valid root message: {len(parentless_roots)}\n")

    if broken_links:
        print("🔎 Broken link examples:")
        for i, node_id, link_type, linked_id in broken_links[:10]:
            print(f"[Convo {i}] Node {node_id}: Broken {link_type} -> {linked_id}")

    if parentless_roots:
        print("\n⚠️ Conversations missing root messages:")
        print(parentless_roots)

if __name__ == "__main__":
    integrity_scan()
