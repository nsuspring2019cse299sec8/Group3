from flask import Flask, render_template, request, redirect
from productsData import products_info, category_info
from usersData import RegistrationForm


application = Flask(__name__)


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/products/<category>/')
def products(category):
    category_list = category_info(category)
    product_list = products_info(category)
    return render_template('products.html', product_list=product_list, category_list=category_list)


@application.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('register.html')
    return render_template('register.html', form=form)


if __name__ == '__main__':
    application.run(debug=True)
