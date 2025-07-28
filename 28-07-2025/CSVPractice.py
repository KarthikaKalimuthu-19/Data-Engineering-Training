import pandas as pd

df = pd.read_csv('employees.csv')

print("CSV Read:\n", df)

df.to_csv('updated_employees.csv', index=False)

print("CSV written to updated_employees.csv")