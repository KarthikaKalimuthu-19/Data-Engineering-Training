num = input("Enter numbers: ")

num_list = list(map(int, num.split()))

sorted = sorted(set(num_list))

print("Sorted unique numbers:", sorted)

if len(sorted) >= 2:
    print("Second largest number is:", sorted[-2])
else:
    print("Not enough unique numbers to find second largest.")
