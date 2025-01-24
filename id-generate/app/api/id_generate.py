from fastapi import APIRouter
from ..schemas.id_generate import BaseIdGenerate, IdGenerate, CreateIdGenerate
from ..crud.sequence_id_generator import SequenceIdGenerateMapper
from typing import List

sequenceIdGenerateMapper = SequenceIdGenerateMapper()
router = APIRouter()

@router.get("/gen_id", response_model=BaseIdGenerate)
async def generateId():
    idGenerateResponse: BaseIdGenerate = {
        "id": "uuid",
    }
    return idGenerateResponse

@router.get("/items", response_model=List[IdGenerate])
async def get_items():
    db_items = sequenceIdGenerateMapper.get_items()
    response_items: List[IdGenerate] = []
    for db_item in db_items:
        response_item: IdGenerate = {
            "id": db_item.id,
            "current_max_id": db_item.current_max_id,
            "step": db_item.step,
            "biz_type": db_item.biz_type,
        }
        response_items.append(response_item)
    return response_items

@router.post("/create_item", response_model=CreateIdGenerate)
async def createItem(item: CreateIdGenerate):
    db_item = sequenceIdGenerateMapper.create_item(item)
    response_item: IdGenerate = {
        "id": db_item.id,
        "current_max_id": db_item.current_max_id,
        "step": db_item.step,
        "biz_type": db_item.biz_type,
    }
    return response_item