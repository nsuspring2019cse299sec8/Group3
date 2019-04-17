from databaseConnection import database
from exception import  Error


class Cart(object):
    def __init__(self, session_id):
        self.sessionID = session_id

    def fetch_quantity_left(self, category_id, product_id):
        data_cursor = database.cursor(dictionary=True)
        sql = "SELECT quantityLeft FROM product_details WHERE categoryID=%s AND productID=%s"
        data_cursor.execute(sql, (category_id, product_id,))
        sql_result = data_cursor.fetchone()
        data_cursor.close()
        return sql_result

    def update_quantity_left(self, quantity_left, category_id, product_id):
        data_cursor = database.cursor(dictionary=True)
        sql = "UPDATE product_details SET quantityLeft=%s WHERE categoryID=%s AND productID=%s"
        values = (quantity_left, category_id, product_id)
        data_cursor.execute(sql, values)
        database.commit()
        data_cursor.close()

    def fetch_cart_quantity(self, category_id, product_id):
        data_cursor = database.cursor(dictionary=True)
        sql = "SELECT quantity FROM orders WHERE salesID=%S AND categoryID=%s AND productID=%s"
        data_cursor.execute(sql, (self.sessionID, category_id, product_id,))
        sql_result = data_cursor.fetchone()
        data_cursor.close()
        return sql_result

    def update_cart_quantity(self, cart_quantity, category_id, product_id):
        data_cursor = database.cursor(dictionary=True)
        sql = "UPDATE orders SET quantity=%s WHERE salesID=%s AND categoryID=%s AND productID=%s"
        values = (cart_quantity, self.sessionID, category_id, product_id)
        data_cursor.execute(sql, values)
        database.commit()
        data_cursor.close()

    def insert_into_cart(self, category_id, product_id):
        data_cursor = database.cursor(dictionary=True)
        sql = "INSERT INTO orders(salesID,categoryID,productID,quantity) VALUES (%s, %s, %s, 1)"
        values = (self.sessionID, category_id, product_id, 1)
        data_cursor.execute(sql, values)
        database.commit()
        data_cursor.close()

    def add_to_cart(self, category_id, product_id):
        quantity_left = self.fetch_quantity_left(category_id, product_id)
        if quantity_left > 0:
            cart_quantity = self.fetch_cart_quantity(category_id, product_id)
            if cart_quantity is not None:
                cart_quantity += 1
                self.update_cart_quantity(cart_quantity, category_id, product_id)
                quantity_left -= 1
                self.update_quantity_left(quantity_left, category_id, product_id)
            else:
                self.insert_into_cart(category_id, product_id)
                quantity_left -= 1
                self.update_quantity_left(quantity_left, category_id, product_id)
