import logging
from fastapi import FastAPI
from Lessons.Lections.Lect5.task7 import Item

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.put("/items/{item_id}")   # Put запрос  (для изменения данных в БД
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {"item_id": item_id, "item": item}
