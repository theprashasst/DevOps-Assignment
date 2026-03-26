from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="DevOps Assignment")


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the terminal-style landing page."""
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "ok"}
