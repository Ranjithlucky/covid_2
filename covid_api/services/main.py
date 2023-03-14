from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from schemas import User
from models import Country,Statistics,History
import schemas
import models
from fastapi.responses import JSONResponse
from database import SessionLocal,engine
from typing import List

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
# COUNTRY -ENDPOINT
@app.get("/countries")
async def country(db: Session = Depends(get_db)):
    try:
        execute_query = db.query(Country.country).all()
        country_data = [country.country for country in execute_query]
        country_count = len(country_data)
        return JSONResponse(status_code=200, content={
            "get": "countries",
            "parameters": [],
            "errors": [],
            "results": country_count,
            "response": country_data
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "Internal server error"})
#COMMON NESTED LOOP FUNCTION
def Covid_func(Covid_data):
    list_of_data = []
    for i in Covid_data:
        res = {
            "continent": i.continent,
            "country": i.country,
            "population": i.population,
            "cases": {
                "new": i.new,
                "active": i.active,
                "critical": i.critical,
                "recovered": i.recovered,
                "IM_pop": i.IM_pop,
                "total": i.total
            },
            "deaths": {
                "New_deaths": i.New_deaths,
                "IM_pop_deaths": i.IM_pop_deaths,
                "total_deaths": i.total_deaths
            },
            "tests": {
                "IM_pop_tests": i.IM_pop_tests,
                "total_tests": i.total_tests
            },
            "day": i.date,
            "time": i.datetime
        }
        list_of_data.append(res)
    return list_of_data

def response_model():
    return {
        "get": "statistics",
        "parameters": {
            "country": " "
        },
        "errors": {
            "country": "The country field cannot be empty"
        },
        "results": 0,
        "response": []
    }

#STATISTICS-ENDPOINT

@app.get("/statistics")
async def statistics(db: Session = Depends(get_db)):
    try:
        statistics_data = db.query(Statistics).all()
        return_data = {            
            "get": "statistics",
            "parameters": [],
            "errors": [],
            "results": len(statistics_data),
            "response": Covid_func(statistics_data)           
        }    
        return return_data
    except Exception as Err:
        return response_model()
        
@app.get("/statisticss/{country}")
async def statistics(country: str , db: Session = Depends(get_db)):
    try:
        statisticss_data = db.query(Statistics).filter(Statistics.country == country).all()
        return_data = {            
            "get": "statisticss",
            "parameters": {
                "country": country
            },
            "errors": [],
            "results": len(statisticss_data),
            "response": Covid_func(statisticss_data)           
        }    
        return return_data
    except Exception as Err:
        return response_model() 

#HISTORY-END POINT 

@app.get("/history/country/{country}&date/{date}")
async def history(country,date,db: Session = Depends(get_db)):
    
    try:
        history_data = db.query(History).filter(History.country == country).all()
        return_data = {            
            "get": "history",
            "parameters": {
                "country": country,
                "date": date
            },
            "errors": [],
            "results": len(history_data),
            "response":Covid_func(history_data)           
        }    
        return return_data
    except Exception as Err:
        return "History cannot be find OUT"   
        
