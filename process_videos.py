import json, os
import numpy as np
import faiss
import openai
openai.api_key = "your-api-key"

def transcribe_with_openai(file_path):
    with open(file_path, "rb") as f:
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            response_format="verbose_json"
        )
    return transcript

def get_embedding(text):
    response = openai.embeddings.create(
        input=[text],
        model="text-embedding-3-small"
    )
    return response.data[0].embedding

dimension = 1536
index = faiss.IndexFlatL2(dimension)
metadata = []

video_dir = "data"
for filename in os.listdir(video_dir):
    if not filename.endswith(".mp4"):
        continue

    video_path = os.path.join(video_dir, filename)
    print(f"Transcribing {filename}...")
    result = transcribe_with_openai(video_path)

    for segment in result.get("segments", []):
        text = segment["text"]
        embedding = get_embedding(text)
        index.add(np.array([embedding], dtype='float32'))
        metadata.append({
            "video_id": filename,
            "start": segment["start"],
            "end": segment["end"],
            "text": text
        })
        
os.makedirs("index", exist_ok=True)
faiss.write_index(index, "index/faiss.index")
with open("index/metadata.json", "w") as f:
    json.dump(metadata, f, indent=2)

print("✅ Indexing complete.")
