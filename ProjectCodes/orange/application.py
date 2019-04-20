from flask import Flask, render_template, request, redirect, flash, session
from flask_socketio import SocketIO
from productsData import ProductsData
from cart import Cart
from usersData import RegistrationForm, LoginForm, UserAuthentication
from exception import Error


UPLOAD_FOLDER = '/static/images'
ALLOWED_EXTENSIONS = set('png')
application = Flask(__name__)
socketIO = SocketIO(application)


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/products/<view>/')
def products(view):
    product = ProductsData.view(view)
    category_list = product.category_info()
    product_list = product.products_info()
    return render_template('products.html', category_list=category_list, product_list=product_list)


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
        if user.login_user():
            flash("You're SUCCESSFULLY logged in.", 'success')
            return redirect('/')
        else:
            flash("Passwords do not match", 'danger')
            return redirect('login.html')
    return render_template('login.html', form=form)


@application.route('/logout/')
def logout():
    cart = Cart(session['session_id'])
    session['logged_in'] = False
    session['user_id'] = None
    session['username'] = None
    session['session_id'] = None
    cart.cancel_cart()
    flash("You are Logged Out", 'success')
    return redirect('/')


@application.route('/cart/<action>/')
@application.route('/cart/<action>/<category_id>/<product_id>/')
def cart_view(action, category_id=None, product_id=None):
    if session.get('logged_in') is True:
        cart = Cart(session['session_id'])
        if action == 'view':
            return render_template('cart.html', cart_items=cart.get_cart(), total_amount=cart.get_cart_total_price())
        elif action == 'add':
            try:
                cart.add_to_cart(category_id, product_id)
            except Error as err:
                flash(err.message, 'danger')
                return redirect('/cart/view/')
            else:
                return redirect('/cart/view')
        elif action == 'remove':
            cart.remove_from_cart(category_id, product_id)
            return redirect('/cart/view')
        elif action == 'cancel':
            cart.cancel_cart()
            return redirect('/cart/view')
    else:
        flash("You are not logged in", 'danger')
        return redirect('/')


@application.route('/admin_panel/<action>/')
def admin_panel(action):
    product = ProductsData.view('admin')
    if action == 'view':
        category_list = product.category_info()
        product_list = product.products_info()
        return render_template('admin_panel.html', category_list=category_list, product_list=product_list)
    return render_template('admin_panel.html')


@socketIO.on('disconnect')
def connection_closed():
    if session.get('logged_in') is True:
        logout()


if __name__ == '__main__':
    application.secret_key = "//This_is_really_secret"
    application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    application.run(debug=True)
