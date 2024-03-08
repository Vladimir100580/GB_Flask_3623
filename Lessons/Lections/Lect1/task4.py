from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>/')
def hello(name='незнакомец'):
    return 'Привет, ' + name + '!'


@app.route('/file/<path:file>/')
def set_path(file):
    print(type(file))
    return f'Путь до файла "{file}"'   # Добавление слешей! возможно


@app.route('/number/<float:num>/')
def set_number(num):
    print(type(num))
    return f'Передано число sqrt{num**2}'


if __name__ == '__main__':
    app.run()