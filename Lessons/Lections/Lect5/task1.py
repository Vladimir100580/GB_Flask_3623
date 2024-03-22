from fastapi import FastAPI

app= FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Запуск сервера
# uvicorn task1:app --reload
