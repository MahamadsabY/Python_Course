
# The given number is prime or not
n = int(input("Enter the Number: "))

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")