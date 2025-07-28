import pandas as pd
import json

df = pd.read_csv("students_cleaned.csv")
df.to_json("students.json", orient="records", indent=2)
