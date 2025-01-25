# Understanding recursion using factorial problem
# The Function which call it-self is call recursion

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)


n = int(input("Enter the number: "))
print(f"The factorial of {n} is :{factorial(n)}")    