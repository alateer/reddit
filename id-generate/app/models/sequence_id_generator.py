from sqlalchemy import Column, Integer, String
from ..db.base_class import Base

class SequenceIdGenerator(Base):
    __tablename__ = "sequence_id_generator"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    current_max_id = Column(Integer)
    step = Column(Integer)
    biz_type = Column(String)