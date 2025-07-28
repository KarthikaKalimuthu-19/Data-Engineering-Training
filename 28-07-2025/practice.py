import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'karthika1923',
    database = 'simple_sql'
)

cursor = conn.cursor()

#create_table_query = """
#CREATE TABLE IF NOT EXISTS employees (
 #   id INT AUTO_INCREMENT PRIMARY KEY,
 #   name VARCHAR(100),
  #  department VARCHAR(100),
  #  salary FLOAT
#);
#"""

#insert_query = """
#INSERT INTO employees (name, department, salary)
#VALUES
 #   ('Rahul Sharma', 'Engineering', 75000),
  #  ('Priya Varma', 'Marketing', 60000),
 #   ('Anil Kapoor', 'HR', 50000);
#"""

#update_query = """
#UPDATE employees SET salary = 55000 WHERE id = 12;
#"""

delete_query = """
DELETE FROM employees WHERE id = 11;
"""
cursor.execute(delete_query)
conn.commit()
print("Deleted successfully")

cursor.close()
conn.close()


