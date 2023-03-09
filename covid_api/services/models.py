from sqlalchemy import Table,Column,Integer,String,Date,DateTime
from sqlalchemy.orm import relationship
from database import Base

class Country(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True)
    continent=Column(String(255))
    

class Statistics(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True)
    continent=Column(String(255))
    country=Column(String(255))
    population=Column(Integer)
    new=Column(Integer)
    active=Column(Integer)
    critical=Column(Integer)
    recovered=Column(Integer)
    IM_pop=Column(Integer)
    total=Column(Integer)
    New_deaths=Column(Integer)
    IM_pop_deaths=Column(Integer)
    total_deaths=Column(Integer)
    IM_pop_tests=Column(Integer)
    total_tests=Column(Integer)
    Date=Column(Integer)
    DateTime=Column(Integer)

class History(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True)
    continent=Column(String(255))
    country=Column(String(255))
    population=Column(Integer)
    new=Column(Integer)
    active=Column(Integer)
    critical=Column(Integer)
    recovered=Column(Integer)
    IM_pop=Column(Integer)
    total=Column(Integer)
    New_deaths=Column(Integer)
    IM_pop_deaths=Column(Integer)
    total_deaths=Column(Integer)
    IM_pop_tests=Column(Integer)
    total_tests=Column(Integer)
    Date=Column(Integer)
    DateTime=Column(Integer)
