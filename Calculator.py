name = str(input("Enter Your Name: "))
print(f"Hello {name} Welcome to Calculator where you can perform operations on two numbers.")

def addition():
    print("You selected Addition operator")
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    return a+b
def substraction():
    print("You selected substraction operator")
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    return a-b
def multiplication():
    print("You selected multiplication operator")
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    return a*b
def division():
    print("You selected division operator")
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    return a/b
def average():
    print("You selected Avarage operator")
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    sum = a+b
    return sum/2
def square():
    print("You selected square operator")
    a=int(input("Enter 1st number: "))
    return a*a

option=input("Select the operator which you want:\na.Addition\nb.Substraction\nc.multiplication\nd.division\ne.Average\nf.Square\n")

if option == "a":
    print(addition())
elif option == "b":
    print(substraction())
elif option == "c":
    print(multiplication())
elif option == "d":
    print(division())
elif option == "e":
    print(average())
elif option == "f":
    print(square())