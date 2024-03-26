from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")             # http://127.0.0.1:8000/items/?q=fhgfjgfffhddfh
async def read_items(q: str = Query(..., min_length=3, max_length=50)):  # теперь q - обязательный ключ
    results = {"items": [{"item_id": "Spam"}, {"item_id": "Eggs"}]}
    if q:
        results.update({"q": q})
    return results
