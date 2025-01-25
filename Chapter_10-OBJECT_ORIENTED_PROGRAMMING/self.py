class Employee:
    language = "py"
    D_O_B = "28/09/2001"

    def __init__(self):
        print("I am an creating an object")  # dunder method is automatically created

    def getInfo(self):
        print(f"The langauage is {self.language}. the sallary is {self.D_O_B}")

    @staticmethod
    def greet():
        print("Good Morning")


mammu = Employee()   #mammu is object
# mammu.name = "Mahamadsab"
# print(mammu.language, mammu.D_O_B)
# mammu.greet()
# mammu.getInfo() 