class Calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"the sqaure is : {self.n*self.n}")

    def cube(self):
        print(f"the cube is : {self.n*self.n*self.n}") 

    def square_root(self):
        print(f"the sqaure_root is : {self.n**1/2}")    

a = Calculator(4)    
a.square()
a.cube()
a.square_root()    