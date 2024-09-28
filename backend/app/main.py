# Standard library

# FastAPI library
from fastapi import FastAPI

# App
from app.database.db import execute_query
from app.models.education import Institution


app = FastAPI()


# HOME

@app.get("/")
async def root():
    return {"message": "Hello World"}


# EDUCATION

@app.get("/education")
async def read_education_all():
    return {"Institutions": [inst for inst in Institution]}


@app.get("/education/{institution_id}")
async def read_education_by_institution(institution_id: Institution):
    query = f'''
        SELECT I.description, E.title, E.start, E.end
        FROM "Education" as E 
        JOIN "Institution" as I
        ON E.institution = I.name
        WHERE I.name::text = '{institution_id.value}';
        '''
    print(execute_query(query)) # Data of the Education in that institution
    return {"Institution": institution_id.value}


