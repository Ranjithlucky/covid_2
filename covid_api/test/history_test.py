from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_history():
    
    response = client.get("/history/country/US&date/2022-01-01")
    assert response.status_code == 200
    assert len(response.json()["response"]) > 0

    #  no data exists
    response = client.get("/history/country/Canada&date/2022-01-00")
    assert response.status_code == 404
    assert response.json() == {
        "Message": "No data found"
    }
}
