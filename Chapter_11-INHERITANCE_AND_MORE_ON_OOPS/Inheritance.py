class Vehicle:
    start = "start the car"
    stop = "stop the car"

    def show(self):
        print(f"{self.start} and {self.stop}")


class defender(Vehicle):
    def show2(self):
        print(f"This is the inheritance of {self.start} and {self.stop}")
   

v = Vehicle()
d = defender()

d.show2()

print(d.start)
print(d.stop)



              
