from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db = SQLAlchemy()


class UserRole(Enum):
    STUDENT = 1
    TEACHER = 2
    LISTENER = 3


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     role = db.Column(db.Enum(UserRole), default=UserRole.USER)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    role = db.Column(db.Enum(UserRole), default=UserRole.STUDENT)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
