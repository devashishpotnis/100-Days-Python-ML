E-Commerce Sales Analysis 

Create Database
CREATE DATABASE ecommerce_db;
USE ecommerce_db;

Create Tables
-- Customers Table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);

-- Products Table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

-- Orders Table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Order Details Table
CREATE TABLE order_details (
    order_detail_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

Insert Sample Data
-- Customers
INSERT INTO customers VALUES
(1, 'Amit', 'Pune'),
(2, 'Rahul', 'Mumbai'),
(3, 'Sneha', 'Delhi'),
(4, 'Priya', 'Bangalore');

-- Products
INSERT INTO products VALUES
(101, 'Laptop', 'Electronics', 50000),
(102, 'Phone', 'Electronics', 20000),
(103, 'Shoes', 'Fashion', 3000),
(104, 'Watch', 'Accessories', 5000);

-- Orders
INSERT INTO orders VALUES
(1001, 1, '2024-01-10'),
(1002, 2, '2024-02-15'),
(1003, 3, '2024-03-05'),
(1004, 1, '2024-03-20');

-- Order Details
INSERT INTO order_details VALUES
(1, 1001, 101, 1),
(2, 1001, 103, 2),
(3, 1002, 102, 1),
(4, 1003, 104, 3),
(5, 1004, 101, 1),
(6, 1004, 102, 2);

Analysis Queries

Total Sales
SELECT SUM(p.price * od.quantity) AS total_sales
FROM order_details od
JOIN products p ON od.product_id = p.product_id;

Top Selling Products
SELECT p.product_name, SUM(od.quantity) AS total_quantity
FROM order_details od
JOIN products p ON od.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity DESC;

Customer-wise Spending

SELECT c.name, SUM(p.price * od.quantity) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_details od ON o.order_id = od.order_id
JOIN products p ON od.product_id = p.product_id
GROUP BY c.name
ORDER BY total_spent DESC;

Monthly Sales Trend

SELECT DATE_FORMAT(o.order_date, '%Y-%m') AS month,
       SUM(p.price * od.quantity) AS total_sales
FROM orders o
JOIN order_details od ON o.order_id = od.order_id
JOIN products p ON od.product_id = p.product_id
GROUP BY month
ORDER BY month;

Category-wise Revenue

SELECT p.category, SUM(p.price * od.quantity) AS revenue
FROM order_details od
JOIN products p ON od.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;

Top Customers
SELECT c.name, SUM(p.price * od.quantity) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_details od ON o.order_id = od.order_id
JOIN products p ON od.product_id = p.product_id
GROUP BY c.name
ORDER BY total_spent DESC
LIMIT 3;

Customers Who Spent Above Average
SELECT name, total_spent
FROM (
    SELECT c.name, SUM(p.price * od.quantity) AS total_spent
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_details od ON o.order_id = od.order_id
    JOIN products p ON od.product_id = p.product_id
    GROUP BY c.name
) t
WHERE total_spent > (
    SELECT AVG(total)
    FROM (
        SELECT SUM(p.price * od.quantity) AS total
        FROM orders o
        JOIN order_details od ON o.order_id = od.order_id
        JOIN products p ON od.product_id = p.product_id
        GROUP BY o.customer_id
    ) x
);

Rank Products (Window Function 🔥)
SELECT p.product_name,
       SUM(od.quantity) AS total_quantity,
       RANK() OVER (ORDER BY SUM(od.quantity) DESC) AS rank_position
FROM order_details od
JOIN products p ON od.product_id = p.product_id
GROUP BY p.product_name;

Most Recent Orders
SELECT * FROM orders
ORDER BY order_date DESC
LIMIT 5;
