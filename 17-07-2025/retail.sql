CREATE DATABASE retail_store;
USE retail_store;

create table products (
  product_id int primary key,
  product_name varchar(100),
  category varchar(100),
  price decimal(10,2),
  stock int
);

insert into products values
(1, 'Kurti', 'Clothing', 2000.00, 20),
(2, 'Boat', 'Accessories', 1000.00, 10),
(3, 'Samsung', 'Electronics', 35000.00, 25),
(4, 'Wooden bed', 'Furniture', 40000.00, 9),
(5, 'Necklace', 'Jewellery', 25000.00, 30);

select * from products