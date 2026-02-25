CREATE DATABASE CompanyDB;
USE CompanyDB;

-- Department Table
CREATE TABLE Department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

-- Employee Table
CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    salary INT,
    dept_id INT,
    join_date DATE,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

-- Insert Data
INSERT INTO Department VALUES
(1,'HR'),
(2,'IT'),
(3,'Sales');

INSERT INTO Employee VALUES
(101,'Devashish',50000,2,'2023-01-10'),
(102,'Karan',60000,1,'2022-03-15'),
(103,'Prathmesh',70000,2,'2021-07-20'),
(104,'Swapnil',55000,3,'2023-05-18'),
(105,'Rahul',65000,3,'2022-09-25');