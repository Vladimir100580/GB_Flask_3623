from flask import Flask

app = Flask(__name__)

html = """
<h1>Привет, меня зовут Алексей</h1>
<p>Уже много лет я создаю сайты на Flask.<br/>Посмотрите на мой сайт.</p>
"""
print(html)


@app.route('/text/')
def text():
    return html


if __name__ == '__main__':
    app.run()