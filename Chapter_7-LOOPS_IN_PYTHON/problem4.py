# Factorial of number

n = int(input("Enter the Number: "))
product = 1
for i in range(1,n+1):
    product = product * i

print(f"The factorian of {n} is {product}")    