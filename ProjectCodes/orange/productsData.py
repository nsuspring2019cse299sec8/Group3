from databaseConnection import database


class ProductsData(object):
    def __init__(self, category):
        self.category = category

    def category_info(self):
        data_cursor = database.cursor(dictionary=True)
        if self.category == "women":
            data_cursor.execute("SELECT * FROM product_category WHERE categoryID BETWEEN 1000 AND 1999")
        elif self.category == "men":
            data_cursor.execute("SELECT * FROM product_category WHERE categoryID BETWEEN 2000 AND 2999")
        sql_result = data_cursor.fetchall()
        data_cursor.close()
        return sql_result

    def products_info(self):
        data_cursor = database.cursor(dictionary=True)
        if self.category == "women":
            data_cursor.execute("SELECT * FROM product_details WHERE categoryID BETWEEN 1000 AND 1999")
        elif self.category == "men":
            data_cursor.execute("SELECT * FROM product_details WHERE categoryID BETWEEN 2000 AND 2999")
        sql_result = data_cursor.fetchall()
        data_cursor.close()
        return sql_result
