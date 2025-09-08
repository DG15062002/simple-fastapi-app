# Test file for FastAPI application
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Welcome to DevOps FastAPI Application!"
    assert data["version"] == "1.0.0"

def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["version"] == "1.0.0"
    assert "timestamp" in data

def test_status_check():
    """Test the status endpoint"""
    response = client.get("/status")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "fastapi-devops-app"

def test_create_item():
    """Test item creation endpoint"""
    item_data = {
        "name": "Test Item",
        "description": "A test item",
        "price": 100.0,
        "tax": 0.1
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["item_name"] == "Test Item"
    assert data["price"] == 100.0
    assert data["total_price"] == 110.0

def test_create_item_without_tax():
    """Test item creation without tax"""
    item_data = {
        "name": "No Tax Item",
        "price": 50.0
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["item_name"] == "No Tax Item"
    assert data["total_price"] == 50.0

def test_metrics_endpoint():
    """Test metrics endpoint"""
    response = client.get("/metrics")
    assert response.status_code == 200
    data = response.json()
    assert data["app_version"] == "1.0.0"
    assert data["framework"] == "FastAPI"
    assert data["status"] == "healthy"

def test_invalid_endpoint():
    """Test invalid endpoint returns 404"""
    response = client.get("/invalid")
    assert response.status_code == 404