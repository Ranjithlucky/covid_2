from fastapi.responses import JSONResponse,requests
ENDPOINT='http://127.0.0.1:8000/countries'

def test_get_countries():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_get_countries_Notfound():
    response = requests.get(ENDPOINT)
    assert response.status_code == 404
    assert  JSONResponse(content={"Message" : "No data found"})