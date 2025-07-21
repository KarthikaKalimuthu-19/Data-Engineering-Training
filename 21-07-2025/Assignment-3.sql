CREATE DATABASE BookStore;
USE BookStore;

-- PART 1: Design the Database

CREATE TABLE books (
  book_id INT PRIMARY KEY,
  title VARCHAR(100),
  author VARCHAR(100),
  genre VARCHAR(50),
  price DECIMAL(10, 2)
);

CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  city VARCHAR(100)
);

CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id INT,
  book_id INT,
  order_date DATE,
  quantity INT,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
  FOREIGN KEY (book_id) REFERENCES books(book_id)
);

-- PART 2: Insert Sample Data

INSERT INTO books VALUES
(1, 'The Alchemist', 'Paulo Coelho', 'Fiction', 450.00),
(2, 'Clean Code', 'Robert C. Martin', 'Programming', 850.00),
(3, 'The Art of War', 'Sun Tzu', 'Philosophy', 600.00),
(4, 'Data Structures in C', 'Balagurusamy', 'Education', 520.00),
(5, 'Atomic Habits', 'James Clear', 'Self-help', 700.00);

INSERT INTO customers VALUES
(1, 'Karthika', 'karthika@example.com', 'Hyderabad'),
(2, 'Meena', 'meena@example.com', 'Bangalore'),
(3, 'Asha', 'asha@example.com', 'Mumbai'),
(4, 'Jayashree', 'jayashree@example.com', 'Delhi'),
(5, 'Amutha', 'amutha@example.com', 'Chennai');

INSERT INTO orders VALUES
(1, 1, 2, '2023-01-15', 1), 
(2, 2, 1, '2023-02-10', 2),
(3, 3, 3, '2023-03-05', 1),
(4, 4, 2, '2023-04-12', 1),
(5, 5, 5, '2023-05-20', 3),
(6, 1, 4, '2023-06-25', 1),  
(7, 2, 3, '2023-07-01', 2);

-- PART 3: Write and Execute Queries
-- Basic Queries

-- 1. List all books with price above 500.
SELECT * FROM books
WHERE price > 500;

-- 2. Show all customers from the city of ‘Hyderabad’.
SELECT * FROM customers
WHERE city = "Hyderabad";

-- 3. Find all orders placed after ‘2023-01-01’.
SELECT * FROM orders
WHERE order_date > 2023-01-01;

-- Joins & Aggregations

-- 4. Show customer names along with book titles they purchased.
SELECT c.name AS customer_name, b.title AS book_title FROM orders AS o
JOIN customers AS c 
ON o.customer_id = c.customer_id
JOIN books AS b 
ON o.book_id = b.book_id;

-- 5. List each genre and total number of books sold in that genre.
SELECT b.genre, SUM(o.quantity) AS tot_books_sold FROM orders AS o
JOIN books AS b 
ON o.book_id = b.book_id
GROUP BY b.genre;

-- 6. Find the total sales amount (price × quantity) for each book.
SELECT b.title, SUM(b.price * o.quantity) AS total_sales FROM orders AS o
JOIN books AS b 
ON o.book_id = b.book_id
GROUP BY b.title;

-- 7. Show the customer who placed the highest number of orders.
SELECT c.name, COUNT(o.order_id) AS highest_orders FROM orders AS o
JOIN customers AS c 
ON o.customer_id = c.customer_id
GROUP BY c.name
ORDER BY highest_orders DESC
LIMIT 1;

-- 8. Display average price of books by genre.
SELECT genre, AVG(price) AS avg_price FROM books
GROUP BY genre;

-- 9. List all books that have not been ordered.
SELECT * FROM books
WHERE book_id NOT IN (SELECT DISTINCT book_id FROM orders);

-- 10. Show the name of the customer who has spent the most in total.
SELECT c.name, SUM(b.price * o.quantity) AS tot_spt FROM orders AS o
JOIN customers AS c 
ON o.customer_id = c.customer_id
JOIN books AS b 
ON o.book_id = b.book_id
GROUP BY c.name
ORDER BY tot_spt DESC
LIMIT 1;