import turtle

t = turtle.Turtle()
t.shape('turtle')

def draw_s():
    """ draws S
    """
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)


def draw_square():
    """
    draws a square
    """
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)


def draw_circle():
    """
        draw a circle
    """
    for i in range(120):
        t.forward(3)
        t.left(3)
        i += 1


def draw_many_square():
    """ draws a lot of square"""
    distance = 10
    turtle.speed(1)

    for i in range(0, 50, 5):
        turtle.penup()
        turtle.goto(-i, -i)
        turtle.pendown()
        turtle.forward(distance)
        turtle.left(90)
        turtle.forward(distance)
        turtle.left(90)
        turtle.forward(distance)
        turtle.left(90)
        turtle.forward(distance)
        print(turtle.pos(), end="")
        print(f"{distance =}")
        distance += 10

if __name__ == '__main__':
    draw_many_square()