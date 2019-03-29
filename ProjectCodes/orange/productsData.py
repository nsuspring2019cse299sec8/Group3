from databaseConnection import dataCursor


def category_info(category):
    if category == "women":
        dataCursor.execute("SELECT * FROM product_category WHERE categoryID BETWEEN 1000 AND 1999")
    elif category == "men":
        dataCursor.execute("SELECT * FROM product_category WHERE categoryID BETWEEN 2000 AND 2999")
    sql_result = dataCursor.fetchall()
    return sql_result


def products_info(category):
    if category == "women":
        dataCursor.execute("SELECT * FROM product_details WHERE categoryID BETWEEN 1000 AND 1999")
    elif category == "men":
        dataCursor.execute("SELECT * FROM product_details WHERE categoryID BETWEEN 2000 AND 2999")
    sql_result = dataCursor.fetchall()
    return sql_result
