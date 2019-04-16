** Product Categories 1000 to 1999 are for women.
** Product Categories 2000 to 2999 are for men.
** Product Categories 8000 is for Deleted products.

Fetching all product categories for women
Select*
From 'product_category'
Where catagory _id Between 1000 AND 1999


Fetching all product categories for men
Select *
From 'product_category'
Where catagory _id Between 2000 AND 2999


Fetching all product details for women
Select *
From 'product_details'
Where catagory _id Between 1000 AND 1999


Fetching all product details for men
Select *
From 'product_details'
Where catagory _id Between 2000 AND 2999


Fetching the password of a given user_id  from user_details
select password 
from user_details
where User-id=1

Fetching the password of a given user_id  from user_details
select password 
from user_details
where User-id=2

Inserting values of every column of table Cart
Insert Into cart(salesid ,userid , totalAmmount, date)
VALUES(10 ,1 ,300 ,10-01-19) 


Inserting values of every column of table Cart
Insert Into cart(salesid ,userid , totalAmmount, date)
VALUES(30 ,2 ,400 ,15-01-19) 

Fetcing Quantity left/Quantity for a random product
SELECT quantityLeft 
FROM `product_details`
 WHERE categoryID=1001

Updating quantity of a product
UPDATE 'Product_details'
SET quantityleft=120
WHERE category_Id=1001

Updating quantity of a product for unique category_id and product_id
UPDATE 'Product_details'
SET quantityleft=130
WHERE category_Id=1001 AND product_id=2

Updating Name of a product for unique category_id and product_id
UPDATE 'Product_details'
SET Product1=ProductP
WHERE category_Id=1001 AND product_id=1

Updating cost of a product for unique category_id and product_id
UPDATE 'Product_details'
SET cost=200
WHERE category_Id=1001 AND product_id=1



