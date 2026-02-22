Create Sample Table

CREATE TABLE employees (
    id INT,
    name VARCHAR(50),
    salary INT,
    age INT
);

INSERT INTO employees VALUES
(1, 'Devashish', 30000, 22),
(2, 'Anand', 40000, 25),
(3, 'Manav', 35000, 23),
(4, 'Varad', 50000, 28);



1. COUNT()
Total number of rows

SELECT COUNT(*) AS total_employees
FROM employees;


2. SUM()
Total salary of all employees

SELECT SUM(salary) AS total_salary
FROM employees;


3. AVG()
Average salary

SELECT AVG(salary) AS average_salary
FROM employees;

4. MIN()
Lowest salary

SELECT MIN(salary) AS lowest_salary
FROM employees;

5. MAX()
Highest salary

SELECT MAX(salary) AS highest_salary
FROM employees;