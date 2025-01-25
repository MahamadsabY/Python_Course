# convert inches to centimetre

def inch_to_cm(inch):
    return inch * 2.54

n = int(input("Enter the values in inches : "))

print(f"The corresponding value in cm is : {inch_to_cm(n)}")