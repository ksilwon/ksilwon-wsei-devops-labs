from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello WSEI! Projekt DevOps dziala."}

@app.get("/products")
def get_products():
    return [
        {"id": 1, "name": "Laptop", "status": "Available"},
        {"id": 2, "name": "Myszka", "status": "Sold out"}
    ]
