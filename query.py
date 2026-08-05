from fastapi import FastAPI

app= FastAPI()

all_customers= [
    {"id": 101, "name": "Anuj","city": "Butwal","risk": "low"},
    {"id": 102, "name": "Anij","city": "Butwal","risk": "high"},
    {"id": 103, "name": "Aastha","city": "Butwal","risk": "medium"},
    {"id": 104, "name": "Sandesh","city": "Butwal","risk": "low"},
    {"id": 105, "name": "Anij","city": "Butwal","risk": "medium"},
]

@app.get("/customers")
def get_customers(city: str,risk: str):
    filtered= [
        c for c in all_customers
            if c['city']== city and c['risk']== risk
    ]
    
    return {
        "city": city,
        "risk": risk,
        "count": len(filtered),
        "results": filtered
    }