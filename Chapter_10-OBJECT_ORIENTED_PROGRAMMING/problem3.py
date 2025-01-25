from random import randint
class Train:
    def __init__(self,trainno):
        self.trainno = trainno

    def book(self, fro, to):
        print(f"Ticket is booked in trainno : {self.trainno} from {fro} to {to}")

    def getStatus(self):
        print(f"trainno : {self.trainno} is running successfully")

    def getFare(self, fro, to):
        print(f"Ticket fare in trainno is : {self.trainno} from {fro} to {to} is {randint(222,5556)}")

t = Train(445)
t.book("Gpb","bgm")
t.getStatus()
t.getFare("gpb","bgm")
