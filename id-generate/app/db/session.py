from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:123456@localhost:3306/id_generate"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
