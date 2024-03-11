/*
Table: Customer
id (int) is the primary key column for this table
each row of this table indicates the id of a customer, their name, and the idea of the customer who referred them

Problem statement:
Find the names of the customers that are not referred by the customer with id = 2
Return the result table in any order
*/

SELECT name
FROM Customer
WHERE (referee_id != 2) OR (referee_id is null);