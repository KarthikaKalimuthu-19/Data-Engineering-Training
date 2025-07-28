students = [("Aarav", 80), ("Sanya", 65), ("Meera", 92), ("Rohan", 55)]

for name, score in students:
    if score > 75:
        print(name)

total = sum(score for name, score in students)
average = total / len(students)
print("Average Score:", average)
