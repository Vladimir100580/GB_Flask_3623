# Создать форму для регистрации пользователей на сайте. Форма должна содержать поля "Имя", "Фамилия", "Email",
# "Пароль" и кнопку "Зарегистрироваться". При отправке формы данные должны сохраняться в базе данных,
# а пароль должен быть зашифрован.

from models import db, User
from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        role = request.form['status']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        new_user = User(first_name=first_name, last_name=last_name, role=role, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return 'Регистрация прошла успешно!'
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)

