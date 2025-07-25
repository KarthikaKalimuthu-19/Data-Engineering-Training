username = "admin"
password = "1234"

for i in range(3):
    un = input("Enter username: ")
    pw = input("Enter Password: ")
    if un == username and pw == password:
        print("Login Successfull")
        break
    else:
        print("Invalid entry! Try again")

else:
    print("Account locked")