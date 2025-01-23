from fastapi import APIRouter
from ..schemas.id_generate import IdGenerateResponse, IdGenerate
from ..crud.sequence_id_generator import SequenceIdGenerateMapper
from typing import List

sequenceIdGenerateMapper = SequenceIdGenerateMapper()
router = APIRouter()

@router.get("/gen_id", response_model=IdGenerateResponse)
async def generateId():
    idGenerateResponse: IdGenerateResponse = {
        "id": "uuid",
    }
    return idGenerateResponse

@router.get("/items")
async def get_items():
    db_items = sequenceIdGenerateMapper.get_items()
    response_items: List[IdGenerate] = []
    for db_item in db_items:
        response_item: IdGenerate(
            id = db_item.id,
            current_max_id = db_item.current_max_id,
            step = db_item.step,
            biz_type = db_item.biz_type,
        )
        response_items.append()
        
    return db_items

# @router.post("/create_item")
# async def createItem(item: IdGenerate):
#     s
#     db_item = create_item(db, item)
#     return db_item