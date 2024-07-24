from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class BMICalculationRequest(BaseModel):
    height: float  # height in meters
    weight: float  # weight in kilograms

class BMICalculationResponse(BaseModel):
    bmi: float
    category: str

def calculate_bmi(height: float, weight: float) -> float:
    return weight / (height ** 2)

def categorize_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

@app.post("/calculate_bmi", response_model=BMICalculationResponse)
def calculate_bmi_endpoint(request: BMICalculationRequest):
    bmi = calculate_bmi(request.height, request.weight)
    category = categorize_bmi(bmi)
    return BMICalculationResponse(bmi=bmi, category=category)
