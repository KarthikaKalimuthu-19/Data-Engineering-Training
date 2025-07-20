create database company;
use company;

create table departments(
dept_id int primary key,
dept_name varchar(100)
);

insert into departments values
(1,'Human Resources'),
(2,'Engineering'),
(3,'Marketing');

create table employees(
emp_id int primary key,
emp_name varchar(100),
dept_id int,
salary int,
foreign key (dept_id) references departments(dept_id)
);

insert into employees values
(101,'Amit Sharma',1,30000),
(102,'Neha Reddy',2,45000),
(103,'Faizen Ali',2,48000),
(104,'Divya Mehta',3,35000),
(105,'Ravi Varma',null,28000);

-- ----------------------tasks--------------------------

-- 1.
select e.emp_id,e.emp_name,e.dept_id,e.salary, d.dept_name from employees as e
join departments as d
on d.dept_id = e.dept_id;

-- 2.
select e.emp_id,e.emp_name from employees as e
left join departments as d
on d.dept_id = e.dept_id
where e.dept_id is null;

-- 3.
select d.dept_name, count(e.emp_id) as tot_emp from departments as d
left join employees as e
on d.dept_id = e.dept_id
group by d.dept_name;

-- 4.
select * from departments as d
right join employees as e
on e.dept_id = d.dept_id;

-- 5.
select e.emp_name,d.dept_name from departments as d
join employees as e
on d.dept_id = e.dept_id
where e.salary>40000;