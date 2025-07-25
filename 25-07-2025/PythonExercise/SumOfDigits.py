num = input("Enter a number: ")
total = 0
digits = []

for i in num:
    total = total + int(i)
    digits.append(i)

print("+".join(digits),"=",total)