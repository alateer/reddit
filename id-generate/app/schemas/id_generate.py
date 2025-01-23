from pydantic import BaseModel

class IdGenerateResponse(BaseModel):
    id: str

class IdGenerate(BaseModel):
    id: int
    current_max_id: int
    step: int
    biz_type: str
