import turtle

t = turtle.Turtle()
t.shape('turtle')

""" draws S
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
"""

""" draws a square
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
"""

""" draw a circle 
for i in range(120):
    t.forward(3)
    t.left(3)
    i += 1
"""

""" draws a lot of square"""
length = 10
x = 0
y = 0
for i in range(5,25,5):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    x -=i
    y +=i
    length += i*2
