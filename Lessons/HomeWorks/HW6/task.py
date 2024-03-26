# Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
# — Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
# — Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
# — Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
# • Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
# • Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
# • Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
#
# Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.
# Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.
# from random import randint
# import random

from typing import List
from datetime import date, datetime
import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field

# Используется MySql БД с хостинга beget (там проще делается допуск с любых IP)
from sqlalchemy import ForeignKey

DATABASE_URL = 'mysql+pymysql://{user}:{password}@{server}/{database}'.format(
    user='vovar3573_gbflhw',
    password='gbflhw2024!',
    server='vovar3573.beget.tech',
    database='vovar3573_gbflhw')

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users",
                         metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("name", sqlalchemy.String(32)),
                         sqlalchemy.Column("surname", sqlalchemy.String(32)),
                         sqlalchemy.Column("email", sqlalchemy.String(128)),
                         sqlalchemy.Column("password", sqlalchemy.String(64)),
                         )

products = sqlalchemy.Table("products",
                            metadata,
                            sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                            sqlalchemy.Column("title", sqlalchemy.String(64)),
                            sqlalchemy.Column("description", sqlalchemy.String(512)),
                            sqlalchemy.Column("price", sqlalchemy.Float),
                            )

orders = sqlalchemy.Table("orders",
                          metadata,
                          sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                          sqlalchemy.Column("user_id", ForeignKey("users.id")),  # sqlalchemy.Integer,??
                          sqlalchemy.Column("product_id", ForeignKey("products.id")),
                          sqlalchemy.Column("date", sqlalchemy.String(16)),
                          sqlalchemy.Column("status", sqlalchemy.String(16)),
                          )

engine = sqlalchemy.create_engine(DATABASE_URL)  # connect_args={"check_same_thread": False - только для SqLite
metadata.create_all(engine)  # добавляем таблицу в БД

app = FastAPI()


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    surname: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(max_length=64)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    surname: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(max_length=64)


class ProductIn(BaseModel):
    title: str = Field(max_length=64)
    description: str = Field(max_length=512)
    price: float = Field(gt=0)  # Цена, ну, конечно же - положительна)


class Product(BaseModel):
    id: int
    title: str = Field(max_length=64)
    description: str = Field(max_length=512)
    price: float = Field(gt=0)


class OrderIn(BaseModel):
    user_id: int = Field(ForeignKey("users.id"))
    product_id: int = Field(ForeignKey("users.id"))
    date: date
    status: str = Field(max_length=16)


class Order(BaseModel):
    id: int
    user_id: int = Field(ForeignKey("users.id"))
    product_id: int = Field(ForeignKey("users.id"))
    date: date
    status: str = Field(max_length=16)


@app.on_event("startup")  # Для MySQL и PostgreSQL - эти штуки (startup, shutdown) необходимы
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def read_root():
    return {"Hello!!"}


@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(**user.dict())
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@app.get("/users/", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 5):  # Пример ввода: http://127.0.0.1:8000/users/?skip=7&limit=12.
    query = users.select().offset(skip).limit(limit)
    return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)  # c - колонка
    await database.execute(query)
    return {'message': 'User deleted'}


# Для остальных таблиц сделал только get и post. Собственно, как того и требует задание.
@app.post("/products/", response_model=Product)
async def create_product(product: ProductIn):
    query = products.insert().values(**product.dict())
    last_record_id = await database.execute(query)
    return {**product.dict(), "id": last_record_id}


@app.get("/products/", response_model=List[Product])
async def read_products(skip: int = 5, limit: int = 10):
    query = products.select().offset(skip).limit(limit)
    return await database.fetch_all(query)


@app.post("/orders/", response_model=Order)
async def create_order(order: OrderIn):
    query = orders.insert().values(**order.dict())
    last_record_id = await database.execute(query)
    return {**order.dict(), "id": last_record_id}


@app.get("/orders/", response_model=List[Order])
async def read_orders(skip: int = 2, limit: int = 4):
    query = orders.select().offset(skip).limit(limit)
    return await database.fetch_all(query)


@app.get("/")
async def read_root():
    return {"Hello!!"}


# @app.get("/fake_orders/{count}")
# async def create_note(count: int):
#     for i in range(count):
#         d0 = '01.01.90'     # Диапазон случайной даты
#         d1 = '25.03.24'
#         s0 = datetime.strptime(d0, '%d.%m.%y').date()
#         s1 = datetime.strptime(d1, '%d.%m.%y').date()
#         dat = (s1 - s0) * random.random() + s0
#         sqlalchemy.Column("user_id", ForeignKey("users.id")),  # sqlalchemy.Integer,??
#         sqlalchemy.Column("product_id", ForeignKey("products.id")),
#         sqlalchemy.Column("date", sqlalchemy.String(16)),
#         sqlalchemy.Column("status", sqlalchemy.String(16)),
#         query = orders.insert().values(user_id=randint(26, 40),
#                                        product_id=randint(1, 10),
#                                        date=dat,
#                                        status=random.choice(["being processed", "going to", "completed"]))
#         await database.execute(query)
#     return {'message': f'{count} fake orders create'}
#
#
# @app.get("/fake_products/{count}")
# async def create_note(count: int):
#     for i in range(count):
#         query = products.insert().values(title=f'{generate_rnd_st(10).upper()}_{i}',
#                                          description=f'{generate_rnd_st(80)}',
#                                          price=f'{randint(20, 500) / 100}', )
#         print(users.select())
#         await database.execute(query)
#     return {'message': f'{count} fake products create'}
#
#
# @app.get("/fake_users/{count}")
# async def create_note(count: int):
#     for i in range(count):
#         query = users.insert().values(name=f'{generate_rnd_st(6)}_{i}',
#                                       surname=f'{generate_rnd_st(8)}_{i}',
#                                       email=f'{generate_rnd_st(5)}{i}@mail.ru',
#                                       password=f'{generate_rnd_st(4)}', )
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}
#
# def generate_rnd_st(n: int = 3):  # для фейковых данных
#     """ Генерация случайной строки из n символов (латиница, нижний регистр)"""
#     return ''.join([chr(randint(97, 122)) for _ in range(n)])
