import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("index/faiss.index")
with open("index/metadata.json", "r") as f:
    metadata = json.load(f)

def search_video(query):
    embedding = model.encode([query])
    D, I = index.search(np.array(embedding, dtype='float32'), k=1)
    result = metadata[I[0][0]]
    return {
        "video_id": result["video_id"],
        "timestamp": result["start"],
        "text": result["text"]
    }

if __name__ == "__main__":
    query = input("Enter your query: ")
    result = search_video(query)
    print("🔎 Result:")
    print(result)
