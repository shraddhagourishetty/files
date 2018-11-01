#our first class msdie
import random
import turtle
t = turtle
class msdie3:
    def __init__(self, sides):
        self.sides = sides
        self.value = 1
    def roll(self):
        self.value = random.randrange(1, self.sides + 1)
    def getvalue(self):
        return self.value
    def one_dot():
        for x in range():
            t.forward(100)
            t.lef(90)
        for x in range():
            t.penup()
            t.goto(50, -50)
    one_dot()

    def setvalue(self, value):
        self.value = value

#code to test if this is working
die1 = msdie3(6)
die1.roll()
print("die value is:", die1.getvalue())


