from fastapi import FastAPI, Depends, Query, HTTPException
import pandas as pd
from models.internships import Internships
from models.database import SessionLocal
from Prompt_Managing.filter_functions import filter_by_type, filter_by_location, filter_by_duration
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from Prompt_Managing.prompt_analysis import extract_criteria  # Import de la fonction d'analyse NLP

app = FastAPI(
    title="My title",
    description="My description",
    version="0.0.1",
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"Hello": "Bienvenue sur le projet de Jean Ponroy et Quentin Goire, nous avons l'honneur de vous présenter notre premier prototype de notre projet entrepreunarial."}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/internships/")
def get_internships_with_text_query(
    db: SessionLocal = Depends(get_db),
    query_text: str = Query(None),
):
    internships_query = db.query(Internships).all()
    internships_df = pd.DataFrame([vars(internship) for internship in internships_query])

    criteria = {}
    if query_text:
        criteria = extract_criteria(query_text)
        if criteria.get("Type of Internship"):
            internships_df = filter_by_type(internships_df, criteria["Type of Internship"])
        if criteria.get("Place") and not internships_df.empty:
            internships_df = filter_by_location(internships_df, criteria["Place"])
        if criteria.get("Duration") and not internships_df.empty:
            internships_df = filter_by_duration(internships_df, criteria["Duration"])

    return {
        "data": internships_df.to_dict(orient='records'),
        "extracted_criteria": criteria
    }
@app.get("/clean/")
async def read_root():
    return FileResponse("Static/front.html")

@app.get("/filters/")
def get_filters(db: SessionLocal = Depends(get_db)):
    internships_query = db.query(Internships).all()
    internships_df = pd.DataFrame([vars(internship) for internship in internships_query])

    types = list(internships_df['Type_of_internship'].unique())
    locations = list(internships_df['location'].unique())
    durations = list(internships_df['duration'].unique())

    return {
        "types": types,
        "locations": locations,
        "durations": durations
    }