from pydantic import BaseModel

class BaseIdGenerate(BaseModel):
    id: int

class IdGenerate(BaseIdGenerate):
    current_max_id: int
    step: int
    biz_type: str

class CreateIdGenerate(BaseModel):
    current_max_id: int
    step: int
    biz_type: str
