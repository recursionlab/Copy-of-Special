import os

filename = r"C:\Users\ANN\Hub\ExportedConversation\conversations.json"
lines_per_chunk = 15000  # You can tune if needed
output_dir = r"C:\Users\ANN\Hub\ExportedConversation\chunks"

os.makedirs(output_dir, exist_ok=True)

with open(filename, 'r', encoding='utf-8') as infile:
    lines = []
    for idx, line in enumerate(infile, 1):
        lines.append(line)
        if idx % lines_per_chunk == 0:
            chunk_idx = idx // lines_per_chunk
            with open(os.path.join(output_dir, f"slice_{chunk_idx}.json"), 'w', encoding='utf-8') as chunkfile:
                chunkfile.writelines(lines)
            lines = []
    if lines:
        chunk_idx = (idx // lines_per_chunk) + 1
        with open(os.path.join(output_dir, f"slice_{chunk_idx}.json"), 'w', encoding='utf-8') as chunkfile:
            chunkfile.writelines(lines)