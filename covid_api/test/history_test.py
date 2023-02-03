from fastapi.responses import JSONResponse,requests
ENDPOINT_2='http://127.0.0.1:8000/history/country/Afghanistan&date/{Date}?date=2023-01-18'

return_data = ENDPOINT_2

def test_get_history():
    response = requests.get(ENDPOINT_2)
    assert response.status_code == 200

def test_get_countries_Notfound():
    response = requests.get(ENDPOINT_2)
    assert response.status_code == 404
    assert  JSONResponse(content={"Message" : "No data found"})

