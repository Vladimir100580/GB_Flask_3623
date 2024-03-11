from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name=''):
    if name:
        name = ', ' + name
    return f'Добро пожаловать на главную страницу{name}!'


@app.route('/redirect/')  # Редиректы!
def redirect_to_index():
    return redirect(url_for('index', name='Перенаправлятор'))


# @app.route('/redirect/<name>')
# def redirect_to_hello(name):
# return redirect(url_for('hello', name=name))


if __name__ == '__main__':
    app.run()
