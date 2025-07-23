CREATE DATABASE IF NOT EXISTS retail_store;
USE retail_store;

-- Create MySQL tables for products, stores, sales, and employees

CREATE TABLE products (
	productID INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50),
	category VARCHAR(20),
	price DECIMAL(10, 2),
	cost DECIMAL(10, 2),
	discountPercentage DECIMAL(10, 2),
	createdAt DATETIME
);

CREATE TABLE stores (
	storeID INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50),
	region VARCHAR(200),
	address VARCHAR(200),
	createdAt DATETIME
);

CREATE TABLE employees (
	employeeID INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50),
	storeID INT,
	role VARCHAR(20),
	hireDate DATETIME,
	FOREIGN KEY (storeID) REFERENCES stores(storeID)
);

CREATE TABLE sales (
	saleID INT AUTO_INCREMENT PRIMARY KEY,
	productID INT,
	storeID INT,
	employeeID INT,
	quantity INT,
	saleDate DATETIME,
	FOREIGN KEY (productID) REFERENCES products(productID),
	FOREIGN KEY (storeID) REFERENCES stores(storeID),
	FOREIGN KEY (employeeID) REFERENCES employees(employeeID)
);

CREATE INDEX product_name ON products(name);
CREATE INDEX sales_region ON stores(region);

-- Insert sales data with CRUD operations

INSERT INTO products (name, category, price, cost, discountPercentage, createdAt) VALUES
('Laptop Pro 14', 'Electronics', 1200.0, 900.0, 10.00, NOW()),
('Organic Apples', 'Grocery', 3.5, 2.0, 5.00, NOW()),
('Cotton T-Shirt', 'Apparel', 25.0, 10.0, 15.00, NOW()),
('Bluetooth Speaker', 'Electronics', 60.0, 40.0, 20.00, NOW()),
('LED Bulb Pack', 'Home Goods', 15.0, 8.0, 0.00, NOW());

INSERT INTO stores (name, region, address, createdAt) VALUES
('Urban Mart - NY', 'East Coast', '101 Main St, New York, NY', NOW()),
('SuperSave - LA', 'West Coast', '202 Ocean Ave, LA, CA', NOW()),
('FreshStore - TX', 'South', '303 Sunset Blvd, Austin, TX', NOW()),
('MegaMart - IL', 'Midwest', '404 Windy Rd, Chicago, IL', NOW()),
('BudgetBazaar - FL', 'Southeast', '505 Palm Dr, Miami, FL', NOW());

INSERT INTO sales (productID, storeID, employeeID, quantity, saleDate) VALUES
(1, 1, 1, 2, NOW()),
(2, 2, 2, 100, NOW()),
(3, 3, 3, 30, NOW()),
(4, 4, 4, 5, NOW()),
(5, 5, 5, 20, NOW());

INSERT INTO employees (name, storeID, role, hireDate) VALUES
('John Smith', 1, 'Cashier', NOW()),
('Alice Johnson', 2, 'Manager', NOW()),
('Bob Lee', 3, 'Sales Associate', NOW()),
('Eva Martinez', 4, 'Supervisor', NOW()),
('David Chen', 5, 'Stock Clerk', NOW());

-- Write a stored procedure to calculate daily sales for a store

DELIMITER //

CREATE PROCEDURE dailySale()
BEGIN
	SELECT s1.name, s2.saleDate, SUM(s2.quantity * p1.price) AS dailySales 
	FROM stores s1
	INNER JOIN sales s2 ON s1.storeID = s2.storeID 
	INNER JOIN products p1 ON s2.productID = p1.productID
	GROUP BY s2.saleDate, s1.name;
END //

DELIMITER ;

CALL dailySale();

SELECT * FROM products;
SELECT * FROM sales;
SELECT * FROM stores;
SELECT * FROM employees;
