from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")         # http://127.0.0.1:8000/items/42?q=Priveet
async def read_item(item_id: int, q: str = None):   # Цепочка ключей через знак вопроса
    return {"item_id": item_id, "q": q}
