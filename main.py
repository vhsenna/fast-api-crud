from fastapi import FastAPI

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
