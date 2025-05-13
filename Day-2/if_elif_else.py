#this program asks user for thier name and greets them with the name input..
name = str(input("Enter your Name: "))
print("Hello" , name , "Welcome to python journey!")
age = int(input("ENTER YOUR AGE: "))

if age > 18:
    print("You are Eligible to drive.",name)
elif age < 18:
    print("You're kid , you can't do anything",name)
elif age == 18:
    print("We will se if you capable or not.",name)
