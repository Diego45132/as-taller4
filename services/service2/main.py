from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import YourModel, YourModelCreate, YourModelRead

app = FastAPI(title="Servicio de YourService")
router = APIRouter()

@app.get("/")
def read_root():
    """Endpoint raíz para verificar funcionamiento."""
    return {"message": "Servicio de YourService en funcionamiento."}

@app.get("/health")
def health_check():
    """Endpoint de salud para verificar el estado del servicio."""
    return {"status": "ok"}

@router.get("/items/", response_model=list[YourModelRead])
def get_items(db: Session = Depends(get_db)):
    """Obtiene todos los items."""
    try:
        items = db.query(YourModel).all()
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener items: {str(e)}")

@router.post("/items/", response_model=YourModelRead)
def create_item(item: YourModelCreate, db: Session = Depends(get_db)):
    """Crea un nuevo item."""
    try:
        db_item = YourModel(**item.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear item: {str(e)}")

app.include_router(router, prefix="/api/v1", tags=["items"])
