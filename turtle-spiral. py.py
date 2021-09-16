# testing turtle
import turtle
t = turtle.Pen()
t.speed(0)
for x in range(360):
    t.forward(x)
    #Note : the closer the number is to x has more sides.
    t.right(200)
