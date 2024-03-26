import databases
import sqlalchemy
# import aiomysql
from fastapi import FastAPI
from pydantic import BaseModel, Field

# DATABASE_URL = "sqlite:///mydatabase.db"
# DATABASE_URL = "postgresql://user:password@localhost/dbname"vovar3573_gbflsk


DATABASE_URL = 'mysql+pymysql://{user}:{password}@{server}/{database}'.format(
    user='vovar3573_gbflsk',
    password='gbflsk2024!',
    server='vovar3573.beget.tech',
    database='vovar3573_gbflsk')
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
users = sqlalchemy.Table("users",
                         metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("name", sqlalchemy.String(32)),
                         sqlalchemy.Column("email", sqlalchemy.String(128)),
                         )

engine = sqlalchemy.create_engine(DATABASE_URL)  # connect_args={"check_same_thread": False - только для SqLite
metadata.create_all(engine)  # добавляем таблицу в БД

app = FastAPI()


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


@app.on_event("startup")            # Для MySQL - эти штуки необходимы
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(name=f'user{i}', email=f'mail{i}@mail.ru')
        await database.execute(query)
    return {'message': f'{count} fake users create'}
