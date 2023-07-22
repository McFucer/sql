from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_URL = 'sqlite:///./test.db'

engine = create_engine(SQL_URL)

Session_local = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()
