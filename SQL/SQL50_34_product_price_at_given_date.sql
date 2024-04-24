/* 
Table: Products
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) is the primary key (combination of columns with unique values) of this table.
Each row of this table indicates that the price of some product was changed to a new price at some date.

Problem Statement: Write a solution to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10. Return the result table in any order.
*/

SELECT DISTINCT product_id, 10 AS price 
FROM Products
WHERE product_id NOT IN (
       SELECT DISTINCT product_id
       FROM Products
       WHERE change_date <= '2019-08-16')
UNION
SELECT product_id, new_price AS price
FROM Products
WHERE (product_id, change_date) IN (
       SELECT product_id, max(change_date) AS date
       FROM Products
       WHERE change_date <= '2019-08-16'
       GROUP BY product_id)