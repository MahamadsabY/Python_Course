class Vehicle:
    start = "start the car"
    stop = "stop the car"

    def show(self):
        print(f"{self.start} and {self.stop}")
     
class bmw:
    gear = "Change tha gear"

    def show1(self):
        print(f"{self.gear}")


class defender(Vehicle,bmw):             # Multiple inheritance
    def show2(self):
        print(f"This is the inheritance of {self.start} and {self.stop}")
   

v = Vehicle()
d = defender()
b = bmw()

print(d.start)
print(d.stop)

d.show2()


              
