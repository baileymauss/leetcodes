/* 
Table: Products
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| product_id       | int     |
| product_name     | varchar |
| product_category | varchar |
+------------------+---------+
product_id is the primary key (column with unique values) for this table.
This table contains data about the company's products.

Table: Orders
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| order_date    | date    |
| unit          | int     |
+---------------+---------+
This table may have duplicate rows.
product_id is a foreign key (reference column) to the Products table.
unit is the number of products ordered in order_date.

Problem Statement: Write a solution to get the names of products that have at least 100 units ordered in February 2020 and their amount. Return the result table in any order.
*/

SELECT p.product_name, SUM(o.unit) AS 'unit'
FROM ORDERS o
JOIN Products p ON o.product_id = p.product_id
WHERE MONTH(order_date) = 2 AND YEAR(order_date) = 2020
GROUP BY o.product_id
HAVING unit >= 100;