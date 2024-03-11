from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return 'Введи путь к файлу в адресной строке'


@app.route('/<path:file>/')
def get_file(file):
    print(file)
    # return f'Ваш файл находится в: {escape(file)}!'
    return f'Ваш файл находится в: {file}!'


if __name__ == '__main__':
    app.run()

# http://127.0.0.1:5000/%3Cscript%3Ealert(%22I%20am%20ha%D1%81ker%22)%3C/script%3E/
