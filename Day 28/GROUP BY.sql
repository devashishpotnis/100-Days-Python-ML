Total Salary by Department
SELECT department, SUM(salary) AS total_salary
FROM Employees
GROUP BY department;


Average Salary by Department
SELECT department, AVG(salary) AS avg_salary
FROM Employees
GROUP BY department;


Count Employees in Each Department
SELECT department, COUNT(*) AS employee_count
FROM Employees
GROUP BY department;


Find departments with average salary > 50,000
SELECT department, AVG(salary) AS avg_salary
FROM Employees
GROUP BY department
HAVING AVG(salary) > 50000;