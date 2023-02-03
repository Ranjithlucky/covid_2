from pydantic import BaseModel

class Cases(BaseModel):
    new:int
    active:int
    critical:int
    recovered:int
    IM_pop:int
    total:int

class User(BaseModel):
    id:int
    continent:str
    country:str
    population:int
    cases:Cases
    
    new_deaths:int
    IM_pop_deaths:int
    total_deaths:int
    IM_pop_tests:int
    total_tests:int
    Date:int
    DateTime:int
    