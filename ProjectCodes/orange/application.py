from flask import Flask, render_template, redirect
from productsData import products_info, category_info


application = Flask(__name__)


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/products/<category>/')
def products(category):
    category_list = category_info(category)
    product_list = products_info(category)
    return render_template('products.html', product_list=product_list, category_list=category_list)


if __name__ == '__main__':
    application.run(debug=True)
