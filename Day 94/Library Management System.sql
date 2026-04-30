Library Management System 

--Create Database--
CREATE DATABASE library_db;
USE library_db;

--Create Tables--
CREATE TABLE members (
    member_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50),
    join_date DATE
);

--Books Table--
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(50),
    category VARCHAR(50),
    available_copies INT
);

--Borrow Table--
CREATE TABLE borrow (
    borrow_id INT PRIMARY KEY,
    member_id INT,
    book_id INT,
    borrow_date DATE,
    return_date DATE,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

--Insert Sample Data--

INSERT INTO members VALUES
(1, 'Amit', 'Pune', '2023-01-10'),
(2, 'Rahul', 'Mumbai', '2023-03-15'),
(3, 'Sneha', 'Nagpur', '2023-05-20');

--Books--

INSERT INTO books VALUES
(101, 'Python Basics', 'Guido', 'Programming', 5),
(102, 'SQL Mastery', 'John', 'Database', 3),
(103, 'Data Science Intro', 'Andrew', 'AI', 2);

--Borrow--

INSERT INTO borrow VALUES
(1, 1, 101, '2024-04-01', NULL),
(2, 2, 102, '2024-04-05', '2024-04-10'),
(3, 3, 103, '2024-04-07', NULL);


--Show All Borrowed Books--

SELECT m.name, b.title, br.borrow_date
FROM borrow br
JOIN members m ON br.member_id = m.member_id
JOIN books b ON br.book_id = b.book_id;

--Find Books Not Returned--

SELECT m.name, b.title
FROM borrow br
JOIN members m ON br.member_id = m.member_id
JOIN books b ON br.book_id = b.book_id
WHERE br.return_date IS NULL;

--Count Books Borrowed by Each Member--

SELECT m.name, COUNT(br.book_id) AS total_books
FROM members m
LEFT JOIN borrow br ON m.member_id = br.member_id
GROUP BY m.name;

--Find Most Borrowed Book--

SELECT b.title, COUNT(br.book_id) AS total
FROM borrow br
JOIN books b ON br.book_id = b.book_id
GROUP BY b.title
ORDER BY total DESC
LIMIT 1;

--Available Books--

SELECT title, available_copies
FROM books
WHERE available_copies > 0;

--Update Return Date--

UPDATE borrow
SET return_date = CURDATE()
WHERE borrow_id = 1;

--Delete Member--

DELETE FROM members
WHERE member_id = 3;
