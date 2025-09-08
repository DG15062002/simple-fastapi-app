from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os
import time
from typing import Dict, Any

app = FastAPI(
    title="DevOps FastAPI App",
    description="A sample FastAPI application for DevOps CI/CD pipeline demonstration",
    version="1.0.0"
)

class HealthResponse(BaseModel):
    status: str
    timestamp: float
    version: str
    environment: str

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/", response_model=Dict[str, Any])
def read_root():
    """Root endpoint returning welcome message"""
    return {
        "message": "Welcome to DevOps FastAPI Application!",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health", response_model=HealthResponse)
def health_check():
    """Health check endpoint for Kubernetes probes"""
    return HealthResponse(
        status="healthy",
        timestamp=time.time(),
        version="1.0.0",
        environment=os.getenv("ENVIRONMENT", "development")
    )

@app.get("/status")
def status_check():
    """Status endpoint for monitoring"""
    return {
        "status": "ok",
        "service": "fastapi-devops-app",
        "uptime": time.time()
    }

@app.post("/items/", response_model=Dict[str, Any])
def create_item(item: Item):
    """Create an item with price calculation"""
    total_price = item.price
    if item.tax:
        total_price = item.price + (item.price * item.tax)
    
    return {
        "item_name": item.name,
        "item_description": item.description,
        "price": item.price,
        "tax": item.tax,
        "total_price": total_price
    }

@app.get("/metrics")
def get_metrics():
    """Basic metrics endpoint for monitoring"""
    return {
        "app_version": "1.0.0",
        "python_version": "3.12",
        "framework": "FastAPI",
        "status": "healthy"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=int(os.getenv("PORT", 8000)),
        reload=False
    )
