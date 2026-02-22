Create Sample Tables

CREATE TABLE customers (
    id INT,
    name VARCHAR(50)
);

INSERT INTO customers VALUES
(1, 'Devashish'),
(2, 'Anand'),
(3, 'Manav');
CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    amount INT
);

INSERT INTO orders VALUES
(101, 1, 500),
(102, 2, 700),
(103, 1, 300),
(104, 4, 900);


1. INNER JOIN
Only matching rows

SELECT customers.name, orders.amount
FROM customers
INNER JOIN orders
ON customers.id = orders.customer_id;


2. LEFT JOIN
All customers + matching orders

SELECT customers.name, orders.amount
FROM customers
LEFT JOIN orders
ON customers.id = orders.customer_id;


3. RIGHT JOIN
All orders + matching customers

SELECT customers.name, orders.amount
FROM customers
RIGHT JOIN orders
ON customers.id = orders.customer_id;


4. FULL JOIN
All customers + all orders

SELECT customers.name, orders.amount
FROM customers
FULL JOIN orders
ON customers.id = orders.customer_id;