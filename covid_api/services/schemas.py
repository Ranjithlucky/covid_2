from pydantic import BaseModel

class Cases(BaseModel):
    new:int
    active:int
    critical:int
    recovered:int
    IM_pop:int
    total:int

class Death(BaseModel):
    New_deaths:int
    IM_pop_deaths:int
    total_deaths:int

class Tests(BaseModel):
    IM_pop_tests:int
    total_tests:int

class User(BaseModel):
    id:int
    continent:str
    country:str
    population:int
    cases:Cases
    death:Death
    tests:Tests
    Date:int
    DateTime:int

    class Config:
        orm_mode=True
     