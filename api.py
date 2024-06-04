from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
from duckduckgo_search import DDGS

app = FastAPI()
security = HTTPBasic()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "eliott"
    correct_password = "dcA9X77y2DG8pw"
    if not (credentials.username == correct_username and credentials.password == correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/search")
def search(
    keywords: str, 
    region: str = "wt-wt", 
    safesearch: str = "moderate", 
    timelimit: str = None,
    backend: str = "api",
    max_results: int = None,
    username: str = Depends(authenticate)  # Include the authenticate dependency here
):
    try:
        result = DDGS().text(keywords, region, safesearch, timelimit, backend, max_results)
    except Exception as e:
        result = str(e)
    return result
