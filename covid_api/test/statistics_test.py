from fastapi.responses import JSONResponse,requests
ENDPOINT_1='http://127.0.0.1:8000/statistics'
ENDPOINT_2='http://127.0.0.1:8000/statisticss/country/Afghanistan'

return_data = ENDPOINT_1
return_data = ENDPOINT_2

def test_get_statistics():
    response = requests.get(ENDPOINT_1)
    assert response.status_code == 200
    assert return_data 

def test_get_countries_Notfound():
    response = requests.get(ENDPOINT_1)
    assert response.status_code == 404
    assert  JSONResponse(content={"Message" : "No data found"})

def test_get_statistics():
    response = requests.get(ENDPOINT_2)
    assert response.status_code == 200
    assert return_data 

def test_get_countries_Notfound():
    response = requests.get(ENDPOINT_2)
    assert response.status_code == 404
    assert  JSONResponse(content={"Message" : "No data found"})