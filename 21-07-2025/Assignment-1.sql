CREATE DATABASE Assignment1;
USE Assignment1;

CREATE TABLE employees (
emp_id INT PRIMARY KEY,
emp_name VARCHAR(100),
department VARCHAR(50),
salary INT,
age INT
);

CREATE TABLE departments (
dept_id INT PRIMARY KEY,
dept_name VARCHAR(50),
location VARCHAR(50)
);

INSERT INTO employees VALUES
(101, 'Amit Sharma', 'Engineering', 60000, 30),
(102, 'Neha Reddy', 'Marketing', 45000, 28),
(103, 'Faizan Ali', 'Engineering', 58000, 32),
(104, 'Divya Mehta', 'HR', 40000, 29),
(105, 'Ravi Verma', 'Sales', 35000, 26);

INSERT INTO departments VALUES
(1, 'Engineering', 'Bangalore'),
(2, 'Marketing', 'Mumbai'),
(3, 'HR', 'Delhi'),
(4, 'Sales', 'Chennai');

-- Section A: Basic SQL

-- 1. Display all employees.
SELECT * FROM employees;

-- 2. Show only emp_name and salary of all employees.
SELECT emp_name, salary FROM employees;

-- 3. Find employees with a salary greater than 􀀀40,000.
SELECT * FROM employees
WHERE salary > 40000;

-- 4. List employees between age 28 and 32 (inclusive).
SELECT * FROM employees
WHERE age BETWEEN 28 AND 32;

-- 5. Show employees who are not in the HR department.
SELECT * FROM employees 
WHERE department NOT IN ("HR");

-- 6. Sort employees by salary in descending order.
SELECT * FROM employees
ORDER BY salary DESC;

-- 7. Count the number of employees in the table.
SELECT COUNT(emp_id) FROM employees;

-- 8. Find the employee with the highest salary.
SELECT MAX(salary) FROM employees;

-- Section B: Joins & Aggregations

-- 1. Display employee names along with their department locations (using JOIN).
SELECT e.emp_name, d.location FROM employees AS e
JOIN departments AS d
ON e.department = d.dept_name;

-- 2. List departments and count of employees in each department.
SELECT d.dept_name, COUNT(e.emp_name) AS no_of_emp FROM employees AS e
JOIN departments AS d
ON e.department = d.dept_name
GROUP BY d.dept_name;

-- 3. Show average salary per department.
SELECT d.dept_name, AVG(e.salary) AS avg_sal FROM employees AS e
JOIN departments AS d
ON e.department = d.dept_name
GROUP BY d.dept_name;

-- 4. Find departments that have no employees (use LEFT JOIN).
SELECT e.emp_name, d.dept_name FROM employees AS e
LEFT JOIN departments AS d
ON e.department = d.dept_name;

-- 5. Find total salary paid by each department.
SELECT d.dept_name, SUM(e.salary) AS tot_sal FROM employees AS e
JOIN departments AS d
ON e.department = d.dept_name
GROUP BY d.dept_name;

-- 6. Display departments with average salary > 􀀀45,000.
SELECT d.dept_name, AVG(e.salary) AS avg_sal FROM employees AS e
JOIN departments AS d
ON e.department = d.dept_name
GROUP BY d.dept_name
HAVING avg_sal > 45000;

-- 7. Show employee name and department for those earning more than 􀀀50,000.
SELECT e.emp_name, d.dept_name, e.salary FROM employees AS e
JOIN departments AS d
ON e.department = d.dept_name
WHERE salary > 50000;