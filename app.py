from fastapi import FastAPI, Query
import faiss
from pydantic import BaseModel
import json
import numpy as np
from typing import List
from sentence_transformers import SentenceTransformer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("index/faiss.index")
with open("index/metadata.json", "r") as f:
    metadata = json.load(f)

class SearchResponse(BaseModel):
    video_id: str
    timestamp: float
    text: str

@app.get("/search", response_model=List[SearchResponse])
def search_video(q: str = Query(...), top_k: int = 3):
    embedding = model.encode([q])
    D, I = index.search(np.array(embedding, dtype="float32"), k=top_k)

    results = []
    for idx in I[0]:
        result = metadata[idx]
        results.append({
            "video_id": result["video_id"],
            "timestamp": result["start"],
            "text": result["text"]
        })

    return results
