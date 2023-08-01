from datetime import datetime
from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, Path
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.models import Geoname
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, desc
import pytz

SQLALCHEMY_DATABASE_URL = "sqlite:///geonames.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(docs_url='/')


@app.get("/geonames/{geonameid}")
def read_geoname(geonameid: int, db: Annotated[Session, Depends(get_db)]):
    data = db.query(Geoname).filter(Geoname.geonameid == geonameid).first()
    if data is None:
        raise HTTPException(status_code=404, detail="Город не найден")
    return JSONResponse(content={'data': jsonable_encoder(data)})


@app.get('/cities/{page}/{page_limit}/')
def get_cities(page: Annotated[int, Path(ge=1)],
               page_limit: Annotated[int, Path(ge=1)],
               db: Annotated[Session, Depends(get_db)]
               ):
    start_index = (page - 1) * page_limit
    data = db.query(Geoname).offset(start_index).limit(page_limit).all()
    if not data:
        raise HTTPException(status_code=404)
    return JSONResponse(content={'data': jsonable_encoder(data)})


@app.get('/compare_cities/{city1}/city2/')
def compare_cities(city1: str, city2: str, db: Annotated[Session, Depends(get_db)]):

    city1_data = db.query(Geoname).filter(Geoname.alternatenames.ilike(f'%{city1}%')).order_by(
        desc(Geoname.population)).first()
    if city1_data is None:
        raise HTTPException(status_code=404, detail=f"Город {city1} не найден")

    city2_data = db.query(Geoname).filter(Geoname.alternatenames.ilike(f'%{city2}%')).order_by(
        desc(Geoname.population)).first()
    if city2_data is None:
        raise HTTPException(status_code=404, detail=f"Город {city2} не найден")

    if city1_data.latitude > city2_data.latitude:
        northern_city = city1_data.name
    else:
        northern_city = city2_data.name

    same_timezone = city1_data.timezone == city2_data.timezone

    city1_tz = pytz.timezone(city1_data.timezone)
    city2_tz = pytz.timezone(city2_data.timezone)
    city1_time = datetime.now(city1_tz).hour
    city2_time = datetime.now(city2_tz).hour

    time_difference = abs(city1_time - city2_time)

    return JSONResponse(content={
        'city1': jsonable_encoder(city1_data),
        'city2': jsonable_encoder(city2_data),
        'northern_city': jsonable_encoder(northern_city),
        'same_timezone': same_timezone,
        'time_difference': str(time_difference),
    })


@app.get('/autocomplete_city/{prefix}/')
def autocomplete_city(prefix: str, db: Annotated[Session, Depends(get_db)]):
    cities = db.query(Geoname).filter(Geoname.name.ilike(f"%{prefix}%")).limit(10).all()
    suggestions = [city.name for city in cities]
    return JSONResponse(content={'suggestions': jsonable_encoder(suggestions)})







