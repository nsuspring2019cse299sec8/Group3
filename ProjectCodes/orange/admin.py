

def admin_perform_query(action, new_value, target_category_id, target_product_id, product):
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
        product.update_product_details('quantityLeft', new_value['quantity_left'], target_category_id, target_product_id)
