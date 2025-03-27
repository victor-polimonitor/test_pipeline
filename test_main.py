from fastapi.testclient import TestClient
from main import app

# Best Practice: Create a test client instance
client = TestClient(app)

def test_read_root():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Addition API"}

def test_add_numbers_valid():
    """Test addition endpoint with valid numbers"""
    test_data = {"num1": 5.0, "num2": 3.0}
    response = client.post("/add", json=test_data)
    assert response.status_code == 200
    assert response.json() == {"result": 8.0}

def test_add_numbers_zero():
    """Test addition endpoint with zero values"""
    test_data = {"num1": 0, "num2": 0}
    response = client.post("/add", json=test_data)
    assert response.status_code == 200
    assert response.json() == {"result": 0.0}

def test_add_numbers_negative():
    """Test addition endpoint with negative numbers"""
    test_data = {"num1": -1, "num2": -2}
    response = client.post("/add", json=test_data)
    assert response.status_code == 200
    assert response.json() == {"result": -3.0}

def test_add_numbers_invalid_input():
    """Test addition endpoint with invalid input"""
    test_data = {"num1": "invalid", "num2": 3}
    response = client.post("/add", json=test_data)
    assert response.status_code == 422  # Validation error 