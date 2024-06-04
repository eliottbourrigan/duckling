from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from duckduckgo_search import DDGS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search(keywords: str, region: str = "wt-wt", safesearch: str = "moderate", timelimit: str = None, backend: str = "api", max_results: int = None):
    try:
        result = DDGS().text(keywords, region, safesearch, timelimit, backend, max_results)
    except Exception as e:
        result = str(e)
    return result