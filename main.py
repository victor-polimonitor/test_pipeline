from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define request model (Best Practice: Use Pydantic models for request validation)
class NumberInput(BaseModel):
    num1: int
    num2: int

@app.post("/add")
async def add_numbers(numbers: NumberInput):
    """
    Add two numbers and return the result
    """
    try:
        result = numbers.num1 + numbers.num2
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Optional: Add a root endpoint for API information
@app.get("/")
async def root():
    """
    Root endpoint providing API information
    """
    return {"message": "Welcome to the Addition API"}
