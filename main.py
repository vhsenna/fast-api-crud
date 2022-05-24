from fastapi import FastAPI
import schemas

app = FastAPI()

fake_database = {
    1:{'task': 'Clean kitchen'},
    2:{'task': 'Buy cheese'},
    3:{'task': 'Write blog'},
}

@app.get('/')
def get_items():
    return fake_database

@app.get('/{id}')
def get_item(id:int):
    return fake_database[id]

@app.post('/')
def add_item(item:schemas.Item):
    new_id = len(fake_database.keys()) + 1
    fake_database[new_id] = {'task': item.task}
    return fake_database

@app.put('/{id}')
def update_item(id:int, item:schemas.Item):
    fake_database[id]['task'] = item.task
    return fake_database

@app.delete('/{id}')
def delete_item(id:int):
    del fake_database[id]
    return fake_database
