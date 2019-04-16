from flask import Flask, render_template, request, redirect, flash, session
from productsData import ProductsData
from usersData import RegistrationForm, LoginForm, UserAuthentication


application = Flask(__name__)


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/products/<category>/')
def products(category):
    product = ProductsData(category)
    category_list = product.category_info()
    product_list = product.products_info()
    return render_template('products.html', product_list=product_list, category_list=category_list)


@application.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = UserAuthentication.registration_details(form)
        user.store_record()
        flash("Your are Successfully Registered")
        return redirect('/login/')
    return render_template('register.html', form=form)


@application.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = UserAuthentication.login_details(form)
        user.login_user()
        flash("Your are Logged In")
    return render_template('login.html', form=form)


@application.route('/logout')
def logout():
    flash("You are Logged Out", 'success')


if __name__ == '__main__':
    application.secret_key = "//This_is_really_secret"
    application.run(debug=True)
