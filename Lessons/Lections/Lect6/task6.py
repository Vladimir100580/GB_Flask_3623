import databases
import sqlalchemy
# import aiomysql
from fastapi import FastAPI
from pydantic import BaseModel

# DATABASE_URL = "sqlite:///mydatabase.db"
# DATABASE_URL = "postgresql://user:password@localhost/dbname"vovar3573_gbflsk


DATABASE_URL = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
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
metadata.create_all(engine)


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

