from flask import Flask

from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)


if __name__ == '__main__':
    app.run()