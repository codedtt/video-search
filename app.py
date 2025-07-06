from fastapi import FastAPI, Query
from search import search

app = FastAPI()

@app.get("/search")
def search_video(q: str = Query(..., description="Your query")):
    result = search(q)
    return result
