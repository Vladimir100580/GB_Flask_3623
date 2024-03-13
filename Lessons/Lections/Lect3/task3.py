from flask import Flask
from models_5 import db, User, Post, Comment

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)  # Подружили базу данных (db) с нашим проектом Flask (app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/')
def index():
    return "Hi!"


if __name__ == '__main__':
    app.run(debug=True)
