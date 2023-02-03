from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User
from fastapi.responses import JSONResponse

user=APIRouter()
# countries-end point
@user.get("/countries")
async def country():
    try:
        country= "(SELECT country FROM users)"
        execet_query=conn.execute(country).fetchall()
        country_data=execet_query

        if len(country_data)==0:
            return JSONResponse(status_code=404,content={"message":"no data found"})

        list_of_data=[]

        for i in country_data:
            list_of_data.append(i['country'])

        country_data=len(country_data)
        return JSONResponse(status_code=200,content={"get":"countries","parameters":[],"errors":[],"results":country_data,"response":list_of_data})
    except Exception as Err:
        return {"Error":str(Err)}

# statistics-end point
@user.get("/statistics")
async def statistics():
    try:
        statistics= "(SELECT * FROM users)"
        execet_query=conn.execute(statistics).fetchall()
        country_data=execet_query

        list_of_data = []
        for i in country_data:
            res = {
                "continent": i['continent'],
                "country": i['country'],
                "population": i['population'],
                "cases": {
                    "new": i['new'],
                    "active": i['active'],
                    "critical": i['critical'],
                    "recovered": i['recovered'],
                    "IM_pop": i['IM_pop'],
                    "total": i['total']
                },
                "deaths": {
                    "New_deaths": i['New_deaths'],
                    "IM_pop_deaths": i['Im_pop_deaths'],
                    "total_deaths": i['total_deaths']
                },
                "tests": {
                    "IM_pop_tests": i['IM_pop_tests'],
                    "total_tests": i['total_tests']
                },
                "day": i['Date'],
                "time": i['DateTime']
                }
            list_of_data.append(res)
        contry_count = len(country_data)                
        return_data = {            
            "get": "statistics",
            "parameters": [],
            "errors": [],
            "results": contry_count,
            "response": list_of_data            
        }    

        if len(country_data) == 0:
            return JSONResponse(status_code=404, content={"Message"})                                                     
        return return_data


    except Exception as  Err:
        return{
            "get": "statistics",
            "parameters": {
                "country": ""
            },
            "errors": {
                "country":"The country field cannot be field ,it as an empty"
            },
            "results": 0,
            "response": []      
        }

@user.get("/statisticss/{country}")
async def statistics_paricularly_one(country:str):
    try:
        statisticss= f"(SELECT * FROM users WHERE country='{country}')"
        execet_query=conn.execute(statisticss).fetchall()
        country_data=execet_query
        

        list_of_data = []
        for i in country_data:
            res = {
                "continent": i['continent'],
                "country": i['country'],
                "population": i['population'],
                "cases": {
                    "new": i['new'],
                    "active": i['active'],
                    "critical": i['critical'],
                    "recovered": i['recovered'],
                    "IM_pop": i['IM_pop'],
                    "total": i['total']
                },
                "deaths": {
                    "New_deaths": i['New_deaths'],
                    "IM_pop_deaths": i['Im_pop_deaths'],
                    "total_deaths": i['total_deaths']
                },
                "tests": {
                    "IM_pop_tests": i['IM_pop_tests'],
                    "total_tests": i['total_tests']
                },
                "day": i['Date'],
                "time": i['DateTime']
                }
            list_of_data.append(res)
        contry_count = len(country_data)                
        return_data = {            
            "get": "statistics",
            "parameters": {
                "country": i['country']
            },
            "errors": [],
            "results": contry_count,
            "response": list_of_data            
        }    

        if len(country_data) == 0:
            return JSONResponse(status_code=404, content={"Message"})                                                     
        return return_data


    except Exception as  Err:
        return{
            "get": "statistics",
            "parameters": {
                "country": ""
            },
            "errors": {
                "country":"The country field cannot be field ,it as an empty"
            },
            "results": 0,
            "response": []      
        }

# history-end point
@user.get("/history/country/{country}&date/{Date}")
async def history(country,date):
    try:
        statisticss= f"(SELECT * FROM users WHERE country='{country}' && date='{date}')"
        execet_query=conn.execute(statisticss).fetchall()
        country_data=execet_query
        

        list_of_data = []
        for i in country_data:
            res = {
                "continent": i['continent'],
                "country": i['country'],
                "population": i['population'],
                "cases": {
                    "new": i['new'],
                    "active": i['active'],
                    "critical": i['critical'],
                    "recovered": i['recovered'],
                    "IM_pop": i['IM_pop'],
                    "total": i['total']
                },
                "deaths": {
                    "New_deaths": i['New_deaths'],
                    "IM_pop_deaths": i['Im_pop_deaths'],
                    "total_deaths": i['total_deaths']
                },
                "tests": {
                    "IM_pop_tests": i['IM_pop_tests'],
                    "total_tests": i['total_tests']
                },
                "day": i['Date'],
                "time": i['DateTime']
                }
            list_of_data.append(res)
        contry_count = len(country_data)                
        return_data = {            
            "get": "statistics",
            "parameters": {
                "country": i['country'],
                "day": i['Date']
            },
            "errors": [],
            "results": contry_count,
            "response": list_of_data            
        }    

        if len(country_data) == 0:
            return JSONResponse(status_code=404, content={"Message"})                                                     
        return return_data


    except Exception as  Err:
        return{
            "get": "statistics",
            "parameters": {
                "country": ""
            },
            "errors": {
                "country":"The country field cannot be field ,it as an empty"
            },
            "results": 0,
            "response": []      
        }
