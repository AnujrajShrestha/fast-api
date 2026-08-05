from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def home():
    return {"message": "my frist API is working"}

@app.get("/customer")
def get_customer(customer_id: int):
    return {
        "customer_id": customer_id,
        "name": "Anuj",
        "status": "active"
    }