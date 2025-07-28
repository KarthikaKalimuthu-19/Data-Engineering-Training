import pandas as pd
import numpy as np

raw_data = {
    'EmpID': [201, 202, 203, 204, 205, 206],
    'Name': ['Aarav', 'Sanya', None, 'Karthik', 'Meera', None],
    'Age': [24, np.nan, 29, 22, 31, np.nan],
    'Department': ['Finance', 'Tech', 'HR', None, 'Marketing', None],
    'Salary': ['52000', '73000', 'not available', '48000', '61000', None]
}

df = pd.DataFrame(raw_data)
print("Raw data:\n",df)

#---------------------------cleaning---------------------------

df['Name'] = df['Name'].fillna('Unknown')

df['Department'] = df['Department'].fillna('Not Assigned')

df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

print("\n Cleaned Data:\n",df)