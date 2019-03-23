from flask import Flask, render_template
from data import products_info, category_info


application = Flask(__name__)

categoryList = category_info()
productList = products_info()


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/products/')
def products():
    return render_template('products.html',productList = productList, categoryList = categoryList)


if __name__ == '__main__':
    application.run(debug=True)
