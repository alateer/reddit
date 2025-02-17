from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DB_URL = 'mysql+pymysql://{USER_NAME}:{PASSWORD}@{PART}/{DB_NAME}'
DATABASE_URL = 'mysql+pymysql://root:123456@localhost:3306/id_generate?charset=utf8'

POOL_SIZE = 20
POOL_RECYCLE = 3600
POOL_TIMEOUT = 15
MAX_OVERFLOW = 2
CONNECT_TIMEOUT = 60

class Database():
    
    def __init__(self) -> None:
        self.connection_is_active = False
        self.engine = None
    
    def get_db_connection(self):
        if self.connection_is_active == False:
            try:
                connect_args={ "connect_timeout": CONNECT_TIMEOUT }
                self.engine = create_engine(DATABASE_URL,
                                            pool_size=POOL_SIZE,
                                            pool_recycle=POOL_RECYCLE,
                                            pool_timeout=POOL_TIMEOUT,
                                            max_overflow=MAX_OVERFLOW,
                                            connect_args=connect_args)
                return self.engine
            except Exception as e:
                print("Error connecting to MySQL DB: ", e)
        return self.engine

    def get_db_session(self, engine):
        try:
            Session = sessionmaker(bind=engine)
            session = Session()
            return session
        except Exception as e:
            print("Error getting DB session: ", e)
            return None
