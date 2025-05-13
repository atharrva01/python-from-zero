#This code checks the user password is it is correct or not.

correct_password = "python123"
user_input = ""

print("Welcome! Please enter the password to continue.")

# Keep asking until the user enters the correct password
while user_input != correct_password:
    user_input = input("Enter password: ")
    if user_input != correct_password:
        print("Incorrect password. Try again.")

print("Access granted ✅")
