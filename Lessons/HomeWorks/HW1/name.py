from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def main():
    context = {'title': "Главная страница"}
    return render_template('main.html', **context)


@app.route('/data/')
def data():
    context = {'title': 'Товары'}
    return render_template('data.html', **context)


@app.route('/data/<product>/')
def data_product(product=None):
    context = {'title': product}
    if product == 'jackets':
        context['prod'] = "Куртки"
        jac = {}
        jac['jacket1'] = ['Columbia', 7000, 50]  # Ключи могут понадобиться для дальнейшей ссылки (скажем, на покупку)
        jac['jacket2'] = ['Bazioni', 6000, 52]   # хотя, можно было бы и обойтись двумерным списком.
        jac['jacket3'] = ['Moncler', 5500, 48]
        jac['jacket4'] = ['ARMANI', 12000, 32]
        context['product'] = jac
    if product == 'shoes':
        context['prod'] = "Обувь"
        sh = {}
        sh['sh1'] = ['Ecco', 17000, 43]
        sh['sh2'] = ['Ralf', 7000, 42]
        context['product'] = sh
    if product == 'dresses':
        context['prod'] = "Платья"
        dr = {}
        dr['dr1'] = ['DOLCE_&_ABBANA', 77000, 39]
        dr['dr2'] = ['VESNALETTO', 36000, 38]
        dr['dr3'] = ['PRONOVIAS', 55000, 41]
        context['product'] = dr

    return render_template('product.html', **context)


if __name__ == '__main__':
    app.run()
