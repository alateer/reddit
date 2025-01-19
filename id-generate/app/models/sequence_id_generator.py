from sqlalchemy import Column, Integer, String
from db.base_class import Base

class User(Base):
    __tablename__ = "id_generate"
    
    id = Column(Integer, primary_key=True, index=True)
    current_max_id = Column(Integer, unique=True, index=True, nullable=False)
    step = Column(Integer)
    version = Column(String)
    biz_type = Column(String)