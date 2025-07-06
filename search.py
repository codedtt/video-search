import numpy as np, json, faiss
from openai import OpenAI

openai = OpenAI(api_key="YOUR_OPENAI_API_KEY")

index = faiss.read_index("index/faiss.index")
with open("index/metadata.json", "r") as f:
    metadata = json.load(f)

def get_embedding(text):
    response = openai.embeddings.create(input=[text], model="text-embedding-3-small")
    return np.array([response.data[0].embedding], dtype='float32')

def search(query):
    q_embed = get_embedding(query)
    D, I = index.search(q_embed, k=1)
    result = metadata[I[0][0]]
    return {
        "video_id": result["video_id"],
        "timestamp": result["start"],
        "text": result["text"]
    }
