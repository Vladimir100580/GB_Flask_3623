# Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой
# будет создан cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу приветствия,
# где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл
# с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.

from flask import Flask, request, make_response, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    if request.cookies.get('gb_username', '') == '':
        return redirect(url_for('login'))

    context = {
        'title': 'Приветствие',
        'name': request.cookies.get('gb_username')
    }
    return render_template('main.html',  **context)


@app.route('/getcookie/')
def get_cookies():
    # получаем значение cookie
    name = request.cookies.get('username')
    return f"Значение cookie: {name}"


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        context = {
            'title': 'Приветствие',
            'name': request.form.get('username')
        }
        response = make_response(render_template('main.html',  **context))
        response.set_cookie('gb_username', request.form.get('username'))
        response.set_cookie('gb_email', request.form.get('email'))
        return response
    return render_template('username_form.html')


@app.route('/logout/')
def logout():
    response = make_response(render_template('main.html'))
    response.set_cookie('gb_username', '')
    response.set_cookie('gb_email', '')
    return response


if __name__ == '__main__':
    app.run(debug=True)
