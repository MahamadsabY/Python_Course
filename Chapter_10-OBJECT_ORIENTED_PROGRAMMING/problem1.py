class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode


p = Programmer("Mammu", "123434","76789")
print(p.company,p.name,p.salary,p.pincode)        