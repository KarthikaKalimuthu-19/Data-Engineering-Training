value = input("Enter value to check Palindrome: ")

text = value.replace(" ","").lower()
reverse = text[::-1]

if text == reverse:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")