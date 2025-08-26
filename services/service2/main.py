from fastapi import FastAPI, APIRouter, HTTPException
import os

import os
from fastapi import FastAPI, APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session


from .database import get_db  
from .models import YourModel, YourModelCreate, YourModelRead  


DATABASE_URL = os.getenv("DATABASE_URL")

app = FastAPI()


router = APIRouter()

@app.get("/")
def read_root():
    return {"message": "Servicio de YourService en funcionamiento."}

@app.get("/health")
def health_check():
    """Endpoint de salud para verificar el estado del servicio."""
    return {"status": "ok"}


@router.get("/items/", response_model=list[YourModelRead])
def get_items(db: Session = Depends(get_db)):
    items = db.query(YourModel).all()
    return items


@router.post("/items/", response_model=YourModelRead)
def create_item(item: YourModelCreate, db: Session = Depends(get_db)):
    db_item = YourModel(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


app.include_router(router, prefix="/api/v1")
