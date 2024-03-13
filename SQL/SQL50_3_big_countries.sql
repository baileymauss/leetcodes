/* 
Table: World
name is the primary key (column with unique values) for this table.
Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.

Problem Statement:
A country is big if it has an area of at least 3 million, or it has a population of at least 25 million
Write a solution to find the name, population, and area of the big countries
*/
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;