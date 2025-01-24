from ..models.sequence_id_generator import SequenceIdGenerator
from ..schemas.id_generate import CreateIdGenerate
from ..db.session import Database

database = Database()
engine = database.get_db_connection()

class SequenceIdGenerateMapper():
    
    def __init__(self) -> None:
        self.session = database.get_db_session(engine)

    def get_items(self):
        items = self.session.query(SequenceIdGenerator).all()
        return items

    def create_item(self, create: CreateIdGenerate):
        db_item = SequenceIdGenerator(
            current_max_id = create.current_max_id,
            step = create.step,
            biz_type = create.biz_type
        )
        self.session.add(db_item)
        self.session.commit()
        self.session.refresh(db_item)
        return db_item