class Employee:
    def __init__(self, name, langauage,D_O_B):  # These are constructors
        self.D_O_B=D_O_B
        self.language= langauage
        self.name = name
        print("I am an creating an object")  # dunder method is automatically created

mammu = Employee("mammu","py","1234")   #mammu is object
print(mammu.D_O_B,mammu.name,mammu.language)
