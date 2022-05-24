from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create database engine
engine = create_engine('sqlite:///todo.db')

base = declarative_base()

session_local = sessionmaker(bind=engine, expire_on_commit=False)
