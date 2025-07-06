import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    if (!query) return;
    try {
      const res = await axios.get("http://localhost:8000/search", {
        params: { q: query, top_k: 3 },
      });
      setResults(res.data);
    } catch (err) {
      console.error(err);
      alert("Search failed. Is FastAPI running?");
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

      <div style={{ marginTop: "30px" }}>
        {results.map((res, idx) => (
          <div key={idx} style={{ marginBottom: "20px", textAlign: "left" }}>
            <strong>🎥 {res.video_id}</strong><br />
            ⏱️ {res.timestamp}s<br />
            🧠 {res.text}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
