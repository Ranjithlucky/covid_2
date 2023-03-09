from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_countries():
    # Test case where data exists
    response = client.get("/countries")
    assert response.status_code == 200
    assert response.json() == {
        "get": "countries",
        "parameters": [],
        "errors": [],
        "results": contry_count,
        "response" : list_of_data})
    }

    # Test case where no data exists
    # Replace this with actual test case by mocking the database query
    response = client.get("/countries")
    assert response.status_code == 404
    assert response.json() == {
        "Message": "No data found"
    }
