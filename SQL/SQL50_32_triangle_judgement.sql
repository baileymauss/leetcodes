/* 
Table: Triangle
+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.
 

Problem Statement: Report for every three line segments whether they can form a triangle. Return the result table in any order.
*/

SELECT *, IF((x+y > z) AND (y + z > x) AND (x + z > y), 'Yes', 'No') AS triangle
FROM Triangle;