from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)    # unique - уникальное поле
    email = db.Column(db.String(120), unique=True, nullable=False)  # nullable=False - не пусто
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy=True)   #lazy - ленивый режим не всегода устанавливаем связи, только, когда это необходимо

    def __repr__(self):
        return f'User({self.username}, {self.email})'


class Post(db.Model):  # Статьи
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Post({self.title}, {self.content})'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)  # Привязываем к статье
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Привязываем к автору
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Comment({self.content})'
