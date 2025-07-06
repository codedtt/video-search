import os
import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
dimension = 384
index = faiss.IndexFlatL2(dimension)
metadata = []

video_dir = "data"

for filename in os.listdir(video_dir):
    if not filename.endswith(".txt"):
        continue

    print(f"Processing {filename}...")
    with open(os.path.join(video_dir, filename), "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        text = line.strip()
        if not text:
            continue
        embedding = model.encode(text)
        index.add(np.array([embedding], dtype="float32"))
        metadata.append({
            "video_id": filename.replace(".txt", ".mp4"),
            "start": i * 10,
            "end": (i + 1) * 10,
            "text": text
        })

# Save index and metadata
os.makedirs("index", exist_ok=True)
faiss.write_index(index, "index/faiss.index")
with open("index/metadata.json", "w") as f:
    json.dump(metadata, f, indent=2)

print("✅ Done building index.")
