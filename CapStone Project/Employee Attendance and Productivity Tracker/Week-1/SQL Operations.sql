CREATE DATABASE employee_attendance;
USE employee_attendance;

-- Create MySQL tables for employees, attendance, and tasks

CREATE TABLE employees (
    employeeID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    role VARCHAR(40),
    email VARCHAR(100),
    hireDate DATETIME DEFAULT NOW(),
    status VARCHAR(20),
    CHECK (status = 'Active' OR status = 'Resigned')
);

CREATE TABLE attendance (
    attendanceID INT AUTO_INCREMENT PRIMARY KEY,
    employeeID INT,
    date DATE,
    clockIN DATETIME,
    clockOUT DATETIME,
    isLate TINYINT(1),
    isAbscent TINYINT(1),
    FOREIGN KEY (employeeID) REFERENCES employees(employeeID)
);

CREATE TABLE tasks (
    taskID INT AUTO_INCREMENT PRIMARY KEY,
    employeeID INT,
    taskName VARCHAR(50),
    taskDate DATE,
    tasksCompleted INT,
    hoursSpent DECIMAL(5, 2),
    productivityScore DECIMAL(5, 2),
    FOREIGN KEY (employeeID) REFERENCES employees(employeeID)
);

-- Perform CRUD operations (e.g., clock-in, clock-out)

INSERT INTO employees (name, department, role, email, hireDate, status) VALUES
('John Doe', 'Engineering', 'Software Developer', 'john.doe@example.com', '2023-01-15', 'Active'),
('Jane Smith', 'Marketing', 'Content Strategist', 'jane.smith@example.com', '2022-11-20', 'Active'),
('Alice Johnson', 'HR', 'HR Manager', 'alice.johnson@example.com', '2021-09-10', 'Active'),
('Bob Brown', 'Engineering', 'DevOps Engineer', 'bob.brown@example.com', '2023-05-01', 'Active'),
('Eva Green', 'Finance', 'Accountant', 'eva.green@example.com', '2022-06-30', 'Resigned');

INSERT INTO attendance (employeeID, date, clockIN, clockOUT, isLate, isAbscent) VALUES
(1, '2024-06-01', '2024-06-01 09:02:00', '2024-06-01 17:00:00', 1, 0),
(2, '2024-06-01', '2024-06-01 08:55:00', '2024-06-01 17:10:00', 0, 0),
(3, '2024-06-01', NULL, NULL, 0, 1),
(4, '2024-06-01', '2024-06-01 09:10:00', '2024-06-01 17:05:00', 1, 0),
(5, '2024-06-01', '2024-06-01 08:50:00', '2024-06-01 16:45:00', 0, 0);

INSERT INTO tasks (employeeID, taskName, taskDate, tasksCompleted, hoursSpent, productivityScore) VALUES
(1, 'API Integration', '2024-06-01', 5, 6.0, 0.83),
(2, 'Content Calendar Creation', '2024-06-01', 3, 4.5, 0.67),
(3, 'Policy Review', '2024-06-01', 0, 0.0, 0.0),
(4, 'CI/CD Setup', '2024-06-01', 4, 5.0, 0.80),
(5, 'Invoice Auditing', '2024-06-01', 6, 7.5, 0.80);

CREATE INDEX idx_employeeID ON employees(employeeID);

-- Write a stored procedure to calculate total working hours per employee

DELIMITER //

CREATE PROCEDURE workHrs()
BEGIN
    SELECT 
        e.name, 
        SUM(TIMESTAMPDIFF(MINUTE, a.clockIN, a.clockOUT)) / 60 AS totalHours
    FROM employees e
    JOIN attendance a ON e.employeeID = a.employeeID
    WHERE a.clockIN IS NOT NULL AND a.clockOUT IS NOT NULL
    GROUP BY e.name
    ORDER BY totalHours DESC;
END //

DELIMITER ;

CALL workHrs();

SELECT * FROM employees;
SELECT * FROM attendance;
SELECT * FROM tasks;
