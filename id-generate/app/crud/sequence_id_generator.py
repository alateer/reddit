from sqlalchemy.orm import Session
from ..models.sequence_id_generator import SequenceIdGenerator
from ..schemas.id_generate import IdGenerate

def get_items(db: Session):
    return db.query(SequenceIdGenerator).all()

def create_item(db: Session, create: IdGenerate):
    db_item = SequenceIdGenerator(
        current_max_id = create.current_max_id,
        step = create.step,
        biz_type = create.biz_type
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item