from sqlalchemy import Table,Column,Integer,String,Date,DateTime
from config import meta

users=Table(
    'users',meta,
    Column('id',Integer,primary_key=True),
    Column('continent',String(255)),
    Column('country',String(255)),
    Column('population',Integer),
    Column('new',Integer),
    Column('active',Integer),
    Column('critical',Integer),
    Column('recovered',Integer),
    Column('IM_pop',Integer),
    Column('total',Integer),
    Column('New_deaths',Integer),
    Column('IM_pop_deaths',Integer),
    Column('total_deaths',Integer),
    Column('IM_pop_tests',Integer),
    Column('total_tests',Integer),
    Column('Date',Date),
    Column('DateTime',DateTime)

)