def collatz(number):
    if number % 2 == 0:
        return number//2
    elif number % 2 == 1:
        return number * 3 + 1

try:
    n = int(input("Enter the number: "))
    if n < 1 :
        print("Enter number greator then zero")
    else:
        while n != 1:
            n = collatz(n)
            print(n)
except  ValueError:
    print("Put the xorrect value")
    
    
