/* 
Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.

Problem Statement: Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
*/

DELETE p2
FROM Person p1, Person p2
WHERE p1.Email = p2.Email AND p2.id > p1.id;