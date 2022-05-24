from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_items():
    return ['Item1', 'Item2', 'Item3']
