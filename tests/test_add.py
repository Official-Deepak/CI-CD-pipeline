from fastapi.testclient import TestClient
import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from index import app

client = TestClient(app)

#parameterized multiple test payloads
@pytest.mark.parametrize("payload,expected",[
    ({"num1": 5, "num2": 3},8),
    ({"num1": 0, "num2": 0},0),
    ({"num1": -5, "num2": 5},0),
    ({"num1": 2.5, "num2": 3.5},6.0),
])
def test_add_success(payload,expected):
    response = client.post("/add_no",json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data["status"] == True
    assert data["data"]["total"] == expected
    assert data["message"] == "Addition successful"

#test for missing fields
@pytest.mark.parametrize(
    "payload, missing_field",
    [
        ({"num2": 3}, "num1"),
        ({"num1": 4}, "num2"),
        ({}, "num1"),
    ]
)
def test_add_missing_field(payload, missing_field):
    response = client.post("/add_no", json=payload)
    data = response.json()
    assert response.status_code == 400
    assert data["status"] == False
    assert data["message"] == f"Missing field: {missing_field}"

#test for invalid fields
@pytest.mark.parametrize(
    "payload",
    [
        ({"num1": "a", "num2": 5}),
        ({"num1": 5, "num2": "b"}),
        ({"num1": "a", "num2": "b"}),
    ]
)
def test_add_invalid_type(payload):
    response = client.post("/add_no", json=payload)
    data = response.json()
    assert response.status_code == 400
    assert data["status"] == False
    assert isinstance(data["message"], str)