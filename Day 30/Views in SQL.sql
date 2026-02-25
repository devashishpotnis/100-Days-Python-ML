CREATE VIEW IT_Employees AS
SELECT emp_name, salary
FROM Employee
WHERE dept_id = 2;

SELECT * FROM IT_Employees;