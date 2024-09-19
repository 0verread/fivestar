from utils.secrets import Secrets

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def get_db():
	engine =  create_engine(Secrets.DATABASE_URL)
	session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
	db  = session_local()
	try:
		yield db 
	finally:
		db.close()

