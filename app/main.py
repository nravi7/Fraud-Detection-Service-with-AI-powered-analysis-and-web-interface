from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import time

from .schemas import ScoreRequest, ScoreResponse
from .providers.openai_provider import classify_with_openai
from .providers.hf_provider import classify_with_hf

app = FastAPI(
    title="Fraud Detection Service",
    description="AI-powered fraud detection using OpenAI and rule-based analysis",
    version="1.0.0"
)

# CORS middleware for web interface
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    """Serve the web interface."""
    return FileResponse("static/index.html")

@app.get("/health")
def health():
    """Health check endpoint."""
    return {
        "status": "ok",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat(),
        "message": "Fraud Detection Service is running!"
    }

@app.post("/v1/score", response_model=ScoreResponse)
def score_openai(req: ScoreRequest):
    """Analyze transaction for fraud using OpenAI."""
    start_time = time.time()
    
    try:
        label, score = classify_with_openai(req.transaction)
        processing_time = int((time.time() - start_time) * 1000)
        
        return ScoreResponse(
            label=label,
            score=score,
            provider="openai",
            processing_time_ms=processing_time
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/v1/score/hf", response_model=ScoreResponse)
def score_hf(req: ScoreRequest):
    """Analyze transaction for fraud using rule-based detection."""
    start_time = time.time()
    
    try:
        label, score = classify_with_hf(req.transaction)
        processing_time = int((time.time() - start_time) * 1000)
        
        return ScoreResponse(
            label=label,
            score=score,
            provider="huggingface",
            processing_time_ms=processing_time
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
