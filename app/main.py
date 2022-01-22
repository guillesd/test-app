from fastapi import FastAPI
from typing import Dict

app = FastAPI(title="Test application with FastAPI, Uvicorn and Docker Compose")

@app.get("/")
def test_endpoint() -> Dict:
    return {"data": "Some data"}