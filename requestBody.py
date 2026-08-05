from fastapi import FastAPI
from pydentic import BaseModel

app= FastAPI()

class LaonApplication(BaseModel):
    name: str
    age: int
    income: float
    loan_amount: float
    employeement_years: int
    
@app.post("/predict")
def predict_loan(application: LaonApplication):
    approved=(
        application.income > 50000 and application.employeement_years > 2 and application.age >=21
    )
    
    return{
        "application name": application.name,
        "loan_amount": application.loan_amount,
        "decision": "approved" if approved else "rejected",
        "review_income": application.income 
    }
