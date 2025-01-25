age = int(input("Enter the age : "))

# if-elif-else ladder

if(age>=18):
    print("You are eligible for voting")
    print("Please give your valuable vote")

elif(age<0):
    print("You are enter negative invalid age")

elif(age==0):
    print("You are entered invalid age it is 0!")
    
else:
    print("Your age is below 18, sorry.!")    

print("End of your program...!")     