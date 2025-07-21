create database Assignment1;
use Assignment1;

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
select * from employees;

-- 2. Show only emp_name and salary of all employees.
select emp_name, salary from employees;

-- 3. Find employees with a salary greater than 􀀀40,000.
select * from employees
where salary > 40000;

-- 4. List employees between age 28 and 32 (inclusive).
select * from employees
where age between 28 and 32;

-- 5. Show employees who are not in the HR department.
select * from employees 
where department not in ("HR");

-- 6. Sort employees by salary in descending order.
select * from employees
order by salary desc;

-- 7. Count the number of employees in the table.
select count(emp_id) from employees;

-- 8. Find the employee with the highest salary.
select max(salary) from employees;

-- Section B: Joins & Aggregations

-- 1. Display employee names along with their department locations (using JOIN).
select e.emp_name, d.location from employees as e
join departments as d
on e.department = d.dept_name;

-- 2. List departments and count of employees in each department.
select d.dept_name, count(e.emp_name) as no_of_emp from employees as e
join departments as d
on e.department = d.dept_name
group by d.dept_name;

-- 3. Show average salary per department.
select d.dept_name, avg(e.salary) as avg_sal from employees as e
join departments as d
on e.department = d.dept_name
group by d.dept_name;

-- 4. Find departments that have no employees (use LEFT JOIN).
select e.emp_name, d.dept_name from employees as e
left join departments as d
on e.department = d.dept_name;

-- 5. Find total salary paid by each department.
select d.dept_name, sum(e.salary) as tot_sal from employees as e
join departments as d
on e.department = d.dept_name
group by d.dept_name;

-- 6. Display departments with average salary > 􀀀45,000.
select d.dept_name, avg(e.salary) as avg_sal from employees as e
join departments as d
on e.department = d.dept_name
group by d.dept_name
having avg_sal > 45000;

-- 7. Show employee name and department for those earning more than 􀀀50,000.
select e.emp_name, d.dept_name, e.salary from employees as e
join departments as d
on e.department = d.dept_name
where salary > 50000;