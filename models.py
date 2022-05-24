from sqlalchemy import Column, Integer, String
from database import base

class Item(base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    task = Column(String(250))
