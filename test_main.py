from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello WSEI! Projekt DevOps dziala."}

def test_read_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json()) == 2
