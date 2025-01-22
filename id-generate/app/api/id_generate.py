from fastapi import APIRouter, Depends
from ..schemas.id_generate import IdGenerateResponse, IdGenerate
from ..models.sequence_id_generator import SequenceIdGenerator
from ..db.session import SessionLocal
from sqlalchemy.orm import Session
from ..crud.sequence_id_generator import get_items, create_item


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/gen_id", response_model=IdGenerateResponse)
async def generateId():
    idGenerateResponse: IdGenerateResponse = {
        "id": "uuid",
    }
    return idGenerateResponse

@router.get("/items")
async def getItems(db: Session = Depends(get_db)):
    db_items = get_items(db)
    return db_items

@router.post("/create_item")
async def createItem(item: IdGenerate, db: Session = Depends(get_db)):
    db_item = create_item(db, item)
    return db_item