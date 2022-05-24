from fastapi import FastAPI, Depends
import schemas
import models
from database import engine, base, session_local
from sqlalchemy.orm import Session

base.metadata.create_all(engine)

def get_session():
    session = session_local()
    try:
        yield session
    finally:
        session.close()

app = FastAPI()

@app.get('/')
def get_items(session: Session=Depends(get_session)):
    items = session.query(models.Item).all()
    return items

@app.get('/{id}')
def get_item(id:int, session: Session=Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item

@app.post('/')
def add_item(item:schemas.Item, session: Session=Depends(get_session)):
    item = models.Item(task=item.task)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@app.put('/{id}')
def update_item(id:int, item:schemas.Item, session=Depends(get_session)):
    item_object = session.query(models.Item).get(id)
    item_object.task = item.task
    session.commit()
    return item_object

@app.delete('/{id}')
def deleteItem(id:int, session = Depends(get_session)):
    item_object = session.query(models.Item).get(id)
    session.delete(item_object)
    session.commit()
    session.close()
    return 'Item was deleted'
