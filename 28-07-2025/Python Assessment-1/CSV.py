import pandas as pd

df = pd.read_csv('students.csv')

df['Age'] = df['Age'].fillna(df['Age'].mean())

df['Score'] = df['Score'].fillna('0')

df.to_csv('students_cleaned.csv', index=False)