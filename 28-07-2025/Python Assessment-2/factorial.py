num = int(input("Enter a number: "))

result = 1
for i in range(2, num + 1):
    result *= i

print("Factorial of", num, "is:", result)
