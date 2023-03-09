
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_history_success():
    response = client.get("//history/country/USA&date/2022-01-01")
    assert response.status_code == 200
    assert response.json() == {
        "get": "statistics",
        "parameters": [
               "country": "USA",
               "Date":"2022-01-01"
        ],
        "errors": [],
        "results": len(db.query(Users).all()),
        "response": [ 
            {
                "continent": "ASIA",
                "country": "USA",
                "population": 83000000,
                "cases": {
                    "new": 3000,
                    "active": 5000,
                    "critical": 300,
                    "recovered": 10000,
                    "IM_pop": 4000,
                    "total": 20000
                },
                "deaths": {
                    "New_deaths": 50,
                    "IM_pop_deaths": 500,
                    "total_deaths": 1000
                },
                "tests": {
                    "IM_pop_tests": 3000,
                    "total_tests": 100000
                },
                "day": "2022-01-01",
                "time": "12:00:00"
            },
            
        ]
    } 
    #  no data exist
    response = client.get("//history/country/US&date/2022-01-00")
    assert response.status_code == 404
    assert response.json() == {
        "Message": "No data found"
    }
