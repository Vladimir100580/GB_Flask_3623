from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<name1>/')
@app.route('/index/<name1>/')
# @app.route('/<name1>/')
def html_index(name1='незнакомец'):
    context = {'name': name1}
    return render_template('index1.html', **context)


if __name__ == '__main__':
    app.run()
