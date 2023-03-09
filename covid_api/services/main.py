from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from models import Users
from schemas import User
import models
import schemas
from fastapi.responses import JSONResponse
from database import SessionLocal,engine

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/countries")
async def country(db:Session=Depends(get_db)):
    try:
         
        execute_query=db.query(Users.country).all()
        country_data=execute_query
        if len(country_data) == 0:
            return JSONResponse(status_code=404, content={"Message" : "No data found"})
        list_of_data = []
        for i in country_data:
            list_of_data.append(i['country'])
        contry_count = len(country_data)            
        return JSONResponse(status_code=200, content={ "get": "countries","parameters": [],"errors": [],"results": contry_count,"response" : list_of_data})
    except:
        return response_model
    


@app.get("/statistics")
async def statistics(db:Session=Depends(get_db)):
    try:
        execute_query=db.query(Users).all()
        country_data=execute_query
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
        return response_model

@app.get("/statisticss/{country}")
async def statistics_paricularly_one(country:str,db:Session=Depends(get_db)):
    try:
        
        execet_query=db.query(Users.country).fetchall()
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
        return response_model

@app.get("/history/country/{country}&date/{Date}")
async def history(country,date,db:Session=Depends(get_db)):
    try:
        
        execet_query=db.query(Users.country,date).fetchall()
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
        return response_model
        
def response_model():
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
    
