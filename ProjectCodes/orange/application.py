from flask import Flask, render_template


application = Flask(__name__)


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/products/')
def products():
    return render_template('products.html')


if __name__ == '__main__':
    application.run(debug=True)
