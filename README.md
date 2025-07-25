
# 🎥 AI-Powered Video Search with Timestamp and Live Captions

This project is a fully local, AI-powered system that enables users to search video content using natural language. It retrieves the most relevant video segment, starts playback from the right timestamp, and displays synced live captions — all without needing any cloud APIs.

## 🔧 Tech Stack

| Component      | Tech Used                      |
|----------------|--------------------------------|
| Backend        | FastAPI                        |
| Frontend       | React.js                       |
| Search Engine  | FAISS                          |
| Embeddings     | SentenceTransformers (`MiniLM`)|
| Transcription  | `.txt` files (simulated)       |
| Hosting        | FastAPI static file serving    |

---

## ✨ Features

- 🔍 **Semantic Search**: Search across video content using natural language
- ⏱ **Precise Timestamp Retrieval**: Starts video from the matching segment
- 🎬 **Video Preview**: Embedded HTML5 player for direct playback
- 💬 **Live Captions**: Transcript synced in real time with video playback
- 🧠 **Fully Offline**: No external APIs or rate limits

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/video-search-ai.git
cd video-search-ai
```

### 2. Set Up Backend (FastAPI)

#### Install dependencies:
```bash
pip install -r requirements.txt
```

#### Requirements:
- `faiss-cpu`
- `sentence-transformers`
- `fastapi`
- `uvicorn`

#### Prepare transcripts:
Place transcript files like `video1.txt` in the `data/` folder. Each line represents a 10-second video segment.

#### Generate vector index:
```bash
python process_videos.py
```

#### Run the FastAPI server:
```bash
uvicorn app:app --reload
```

---

### 3. Set Up Frontend (React)

```bash
cd frontend
npm install
npm start
```

Runs on [http://localhost:3000](http://localhost:3000)

---

## 📂 Folder Structure

```
video-search-ai/
├── app.py                  # FastAPI backend
├── process_videos.py       # Embeds transcript segments into FAISS
├── index/                  # FAISS index + metadata
├── data/
│   ├── video1.txt
│   ├── video1.mp4
├── frontend/               # React frontend
│   └── src/App.js
```

---

## 🧪 Example Usage

1. User enters: `reset password`
2. API returns: `video1.mp4` at `10s`
3. Video loads and plays from that point
4. Caption below video:  
   _"If you forgot your password, click reset and follow the instructions."_

---

## ✅ API Endpoints

### `/search?q=...&top_k=3`
Returns the top-k most relevant segments based on query

### `/videos/{filename}.mp4`
Serves video files from the `data/` folder


---not implemented yet --
### `/captions/{video_id}`
Returns all transcript segments for that video

---

## 🔮 Future Ideas

- Highlight full transcript with current line glowing
- Add subtitle overlay (`<track kind="subtitles">`)
- Show full timeline view of matched results
- Upload your own videos with automatic Whisper transcription

---

## 📃 License

MIT License

---

## 🙌 Credits

- [SentenceTransformers](https://www.sbert.net/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [FastAPI](https://fastapi.tiangolo.com/)
- [React](https://react.dev/)
