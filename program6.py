#shraddha date:11/10/2018 test1v2.py
import turtle
path = "\PYTHON PYCHARM\Files\Test1V2_shraddha.txt"
file_colors = open(path ,'r')
colors = file_colors.readline()
print(colors)
colors1 = file_colors.readline()
print(colors1)
colors2 = file_colors.readline()
print(colors2)
colors3 = file_colors.readline()
print(colors3)
colors4 = file_colors.readline()
print(colors4)
colors5 = file_colors.readline()
print(colors5)

#drawing circle
turtle.color("red")
color = turtle.begin_fill()
shape = turtle.circle(20)
turtle.setposition(33,66)
turtle.end_fill()
turtle.hideturtle()

#drawing square
turtle.color("pink")
turtle.begin_fill()
turtle.setposition(44, 55)
T = turtle.left(90)
T = turtle.forward(29)
T = turtle.left(90)
T = turtle.forward(29)
T = turtle.left(90)
T = turtle.forward(29)
T = turtle.left(90)
T = turtle.forward(29)
T = turtle.end_fill()
turtle.hideturtle()

#drawing rectangle
turtle.color("orange")
turtle.setposition(77, 22)
turtle.begin_fill()
T = turtle.left(90)
T = turtle.forward(29)
T = turtle.left(90)
T = turtle.forward(39)
T = turtle.left(90)
T = turtle.forward(29)
T = turtle.left(90)
T = turtle.forward(39)
T = turtle.end_fill()
turtle.hideturtle()

#drawing triangle
turtle.color("yellow")
turtle.setposition(108, 99)
turtle.begin_fill()
T = turtle.left(60)
T = turtle.forward(29)
T = turtle.left(60)
T = turtle.forward(29)
T = turtle.left(60)
T = turtle.end_fill()
turtle.hideturtle()



print(shape)
turtle.speed(3)

file_colors.close()
