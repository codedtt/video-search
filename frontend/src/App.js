import React, { useState, useRef } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const videoRef = useRef(null);

  const handleSearch = async () => {
    if (!query) return;
    try {
      const res = await axios.get("http://localhost:8000/search", {
        params: { q: query, top_k: 1 },
      });
      setResults(res.data instanceof Array ? res.data : [res.data]);
    } catch (err) {
      console.error(err);
      alert("Search failed. Is FastAPI running?");
    }
  };

  const handlePlay = (timestamp) => {
    if (videoRef.current) {
      videoRef.current.currentTime = timestamp;
      videoRef.current.play();
    }
  };

  return (
    <div className="App">
      <h1>🎬 Video Search</h1>
      <input
        type="text"
        placeholder="Search..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={{ padding: "10px", width: "300px", marginRight: "10px" }}
      />
      <button onClick={handleSearch}>Search</button>

      {results.length > 0 && (
        <>
          <div style={{ marginTop: "20px", textAlign: "left" }}>
            <strong>🎥 {results[0].video_id}</strong><br />
            ⏱️ Timestamp: {results[0].timestamp}s<br />
            🧠 Text: {results[0].text}<br />
            <button onClick={() => handlePlay(results[0].timestamp)} style={{ marginTop: "10px" }}>
              ▶️ Jump to Timestamp
            </button>
          </div>
        </>
      )}
    </div>
  );
}

export default App;
