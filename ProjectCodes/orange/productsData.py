from databaseConnection import database


class ProductsData(object):
    def __init__(self, category_id, product_id, name, price, cost, quantity_left, view):
        self.view = view
        self.categoryID = category_id
        self.productID = product_id
        self.name = name
        self.price = price
        self.cost = cost
        self.quantityLeft = quantity_left

    @classmethod
    def customer_view(cls, view):
        return cls(None, None, None, None, None, None, view)

    def category_info(self):
        data_cursor = database.cursor(dictionary=True)
        if self.view == "women":
            data_cursor.execute("SELECT * FROM product_category WHERE categoryID BETWEEN 1000 AND 1999")
        elif self.view == "men":
            data_cursor.execute("SELECT * FROM product_category WHERE categoryID BETWEEN 2000 AND 2999")
        elif self.view == 'admin':
            data_cursor.execute("SELECT * FROM product_category")
        sql_result = data_cursor.fetchall()
        data_cursor.close()
        return sql_result

    def products_info(self):
        data_cursor = database.cursor(dictionary=True)
        if self.view == "women":
            data_cursor.execute("SELECT * FROM product_details WHERE categoryID BETWEEN 1000 AND 1999")
        elif self.view == "men":
            data_cursor.execute("SELECT * FROM product_details WHERE categoryID BETWEEN 2000 AND 2999")
        elif self.view == 'admin':
            data_cursor.execute("SELECT * FROM product_details")
        sql_result = data_cursor.fetchall()
        data_cursor.close()
        return sql_result
