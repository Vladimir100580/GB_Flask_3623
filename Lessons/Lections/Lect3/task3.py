from flask import Flask
from models_5 import db, User, Post, Comment # при инициализации БД импортируе все можели

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase1.db'
db.init_app(app)  # Подружили базу данных (db) с нашим проектом Flask (app)


@app.route('/')
def index():
    return "Hi!"


@app.cli.command("init-db")  #
def init_db():
    db.create_all()
    print('OK1')


if __name__ == '__main__':
    app.run(debug=True)
