a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

if(b == 0):
    raise ZeroDivisionError("The number cannot divisible by zero")
    
else:
    print(f"The division of a and b is {a/b}")