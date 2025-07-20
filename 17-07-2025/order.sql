use analytics_practice;
 
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50)
);
 
 
INSERT INTO customers VALUES
(1, 'Amit Sharma', 'Delhi'),
(2, 'Neha Reddy', 'Hyderabad'),
(3, 'Rahul Iyer', 'Mumbai'),
(4, 'Divya Mehta', 'Chennai');
 
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_name VARCHAR(100),
    order_amount INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
 
INSERT INTO orders VALUES
(101, 1, 'Laptop', 55000),
(102, 2, 'Mouse', 500),
(103, 1, 'Keyboard', 1500),
(104, 3, 'Monitor', 7000),
(105, 2, 'Printer', 8500);

-- Inner join
select c.customer_name, o.product_name, o.order_amount from customers as c
inner join orders as o
on c.customer_id = o.customer_id;

-- left join
select c.customer_name, o.product_name from customers as c
left join orders as o
on c.customer_id = o.customer_id;

-- right join
select c.customer_name, o.product_name from customers as c
right join orders as o
on c.customer_id = o.customer_id;

-- join with filter
select c.customer_name, o.product_name, o.order_amount from customers as c
inner join orders as o
on c.customer_id = o.customer_id
where o.order_amount > 5000;

-- with alias
select o.order_id, c.customer_name, c.city, o.product_name, o.order_amount from customers as c
inner join orders as o
on c.customer_id = o.customer_id;

-- count with join
select c.customer_name, count(o.order_id) as tot_cnt from customers as c
inner join orders as o
on c.customer_id = o.customer_id
group by c.customer_name
having tot_cnt >1;

-- total amount for each customer
select c.customer_name, sum(o.order_amount) as tot_amt 
from customers as c
inner join orders as o
on c.customer_id = o.customer_id
group by c.customer_name;

-- customer who have not made any orders
select c.customer_name from customers as c
left join orders as o
on c.customer_id = o.customer_id
where o.order_id is null;

-- how many orders from each city
select c.city, count(o.order_id) from customers as c
join orders as o
on c.customer_id = o.customer_id
group by c.city;