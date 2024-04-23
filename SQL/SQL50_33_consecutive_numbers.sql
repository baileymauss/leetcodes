/* 
Table: Logs
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column.

Problem Statement: Find all numbers that appear at least three times consecutively. Return the result table in any order.
*/

SELECT DISTINCT L1.num AS ConsecutiveNums
FROM logs L1,
     logs L2,
     logs L3
WHERE L1.id = L2.id + 1 AND
      L2.id = L3.id + 1 AND
      L1.num = L2.num AND
      L2.num = L3.num;