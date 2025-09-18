
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api import news
import os

app = FastAPI(title="Agentic AI News Assistant")
app.include_router(news.router)

# Serve static web UI
web_dir = os.path.join(os.path.dirname(__file__), "web")
app.mount("/web", StaticFiles(directory=web_dir), name="web")

@app.get("/")
def root():
	return FileResponse(os.path.join(web_dir, "index.html"))
