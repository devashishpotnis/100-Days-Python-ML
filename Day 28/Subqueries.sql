Employees with Salary Above Average
SELECT name, salary
FROM Employees
WHERE salary > (
    SELECT AVG(salary)
    FROM Employees
);


Employees in Same Department as Amit
SELECT name
FROM Employees
WHERE department = (
    SELECT department
    FROM Employees
    WHERE name = 'Devashish'
);

Highest Salary Employee
SELECT name, salary
FROM Employees
WHERE salary = (
    SELECT MAX(salary)
    FROM Employees
);

