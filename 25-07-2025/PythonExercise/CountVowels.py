value = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for i in value:
    if i in vowels:
        count = count+1

print("Number of vowels: ",count)