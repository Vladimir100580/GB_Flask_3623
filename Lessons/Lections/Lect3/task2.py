from flask import Flask
from Lessons.Lections.Lect3.models_1 import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)   # Подружили базу данных (db) с нашим проектом Flask (app)


@app.route('/')
def index():
    return "Hi!"


if __name__ == '__main__':
    app.run(debug=True)
