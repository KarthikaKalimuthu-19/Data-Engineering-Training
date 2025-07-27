import pandas as pd
import numpy as np

dfAttendance = pd.read_csv(r"C:\Users\ELCOT\Desktop\GitHub\CapStone Project\Employee Attendance and Productivity Tracker\Week-2\Datasets\attendance.csv")
dfTasks = pd.read_csv(r"C:\Users\ELCOT\Desktop\GitHub\CapStone Project\Employee Attendance and Productivity Tracker\Week-2\Datasets\tasks.csv")
dfEmpl = pd.read_csv(r"C:\Users\ELCOT\Desktop\GitHub\CapStone Project\Employee Attendance and Productivity Tracker\Week-2\Datasets\employees.csv")

dfAttendance.head()

dfTasks.head()

dfEmpl.head()

dfTasks = dfTasks.dropna()
dfAttendance = dfAttendance.dropna()

df = dfAttendance.merge(dfTasks, how="inner", on="employeeID").merge(dfEmpl, how="inner", on="employeeID")

df["workingHours"] = round(abs((pd.to_datetime(df["clockIN"]) - pd.to_datetime(df["clockOUT"])).dt.total_seconds() / 3600), 2)
df["productivityScore"] = round(df["tasksCompleted"] / df["workingHours"], 2)
df["breakTimes"] = round(df["workingHours"] / 4)

df.head()

summary = df.groupby("employeeID").agg(
    hoursSpent=pd.NamedAgg(column="workingHours", aggfunc="mean"),
    productivityScore=pd.NamedAgg(column="productivityScore", aggfunc="mean"),
    abscentCount=pd.NamedAgg(column="isAbscent", aggfunc="sum")
)

summary_final = dfEmpl[["employeeID", "name"]].merge(summary, on="employeeID", how="left")
topPerformer = summary_final.sort_values("productivityScore", ascending=False).iloc[0, :].rename("TopPerformer")
bottomPerformer = summary_final.sort_values(["abscentCount", "productivityScore"], ascending=[False, True]).iloc[0, :].rename("BottomPerformer")

dfAttendance.to_csv(r"C:\Users\ELCOT\Desktop\GitHub\CapStone Project\Employee Attendance and Productivity Tracker\Week-2\Delieverables\cleaned_attendance.csv")
dfTasks.to_csv(r"C:\Users\ELCOT\Desktop\GitHub\CapStone Project\Employee Attendance and Productivity Tracker\Week-2\Delieverables\cleaned_tasks.csv")

print("-----------------Top performer report----------------------")
print(f"Top performer: {topPerformer.iloc[1]}")
for i, j in topPerformer.items():
  if i != "name":
    print(f"{i}: {j}")
print("-----------------------------------------------------------\n")

print("-----------------Bottom performer report-------------------")
print(f"Bottom performer: {bottomPerformer.iloc[1]}")
for i, j in bottomPerformer.items():
  if i != "name":
    print(f"{i}: {j}")
print("-----------------------------------------------------------\n")

