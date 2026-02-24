Create Database
CREATE DATABASE college_db;
USE college_db;

Create Table with All Constraints
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50) UNIQUE,
    credits INT CHECK (credits > 0)
);


CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18),
    course_id INT,
    admission_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);



Insert Sample Data

INSERT INTO courses VALUES
(101, 'Data Science', 4),
(102, 'Machine Learning', 5),
(103, 'Web Development', 3);


INSERT INTO students (student_id, name, email, age, course_id)
VALUES
(1, 'Devashish', 'dev@gmail.com', 20, 101),
(2, 'Prathmesh', 'prathmesh@gmail.com', 22, 102),
(3, 'Anand', 'anand@gmail.com', 19, 103);