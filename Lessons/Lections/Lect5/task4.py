import logging
from fastapi import FastAPI
from Lessons.Lections.Lect5.task7 import Item

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.post("/items/")     # Post запрос
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item
