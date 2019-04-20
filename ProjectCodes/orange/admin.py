import os
from exception import Error
from productsData import ProductsData

UPLOAD_FOLDER = './static/images/'
ALLOWED_EXTENSIONS = {'png', }


def admin_perform_query(action, new_value, target_category_id, target_product_id, product, picture):
    if action == "update_category_id":
        product.update_category('categoryID', new_value['category_id'], target_category_id)
    elif action == "update_category_name":
        product.update_category('categoryName', new_value['category_name'], target_category_id)
    elif action == "update product_id":
        product.update_product_details('productID', new_value['product_id'], target_category_id, target_product_id)
    elif action == "update product_name":
        product.update_product_details('name', new_value['name'], target_category_id, target_product_id)
    elif action == "update product_price":
        product.update_product_details('price', new_value['price'], target_category_id, target_product_id)
    elif action == "update product_cost":
        product.update_product_details('cost', new_value['cost'], target_category_id, target_product_id)
    elif action == "update product_quantity":
        product.update_product_details('quantityLeft', new_value['quantity_left'],
                                       target_category_id, target_product_id)
    elif action == 'add_product':
        admin_add_product(new_value, picture, UPLOAD_FOLDER, ALLOWED_EXTENSIONS)


def admin_add_product(form, picture, upload_folder, allowed_extensions):
    product = ProductsData.new_product(form['category_id'], form['product_id'], form['name'],
                                       form['price'], form['cost'], form['quantity'])
    product.add_product()
    upload_file(picture, upload_folder, allowed_extensions, form['category_id'], form['product_id'])


def allowed_file(filename, allowed_extensions):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions


def upload_file(file, upload_folder, allowed_extensions, category_id, product_id):
    if file.filename == '':
        raise Error("Picture not included")
    if file and allowed_file(file.filename, allowed_extensions):
        filename = f"{category_id}_{product_id}.png"
        file.save(os.path.join(upload_folder, filename))
        return True
    else:
        raise Error("Picture upload not Complete")
