import turtle


def set_home():
    """

    """
    turtle.penup()
    turtle.home()
    turtle.pendown()


def draw_sun():
    set_home()
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    turtle.done()


def draw_s():
    """ draws S
    """
    set_home()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)


def draw_square(side: int):
    """
    draws a square
    side - side size
    """
    set_home()
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)


def draw_circle():
    """
        draw a circle
    """
    set_home()
    for i in range(120):
        turtle.forward(3)
        turtle.left(3)
        i += 1


def draw_many_square(first_side_size, number):
    """
    draws a lot of square
    :param first_side_size: int - the side of the smallest square
    :param number: int - number of squares
    """
    distance = first_side_size
    step = int(first_side_size / 2)
    for i in range(0, step * number, step):
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
        turtle.left(90)
        distance += 10
        """ for debugging
        print(turtle.pos(), end=" ")
        print(turtle.heading(), end="")
        print(f" {distance =}")
        """


def draw_spider(n: int = 12, length: int = 100):
    """
    draw a spider with n legs
    :param n:
    :param length:
    :return:
    """
    for i in range(n):
        turtle.penup()
        turtle.home()
        turtle.pendown()
        turtle.right(360 / n * (i + 1))
        turtle.forward(length)
        turtle.stamp()


def draw_spiral(a: int = 5, n: int = 10):
    """
    draw Archimedean spiral
    :param a: initial radius
    :param n: quantity loops of one arm of an Archimedean spiral
    """
    set_home()
    a1 = a
    turtle.goto(a, 0)
    for i in range(n):
        turtle.dot(1)
        turtle.left(20)
        turtle.forward(3)
        i += 1


def draw_square_spiral(first_side_size: int = 10, number: int = 10):
    distance = first_side_size
    for i in range(number * 4):
        turtle.forward(distance)
        turtle.left(90)
        distance += 5


if __name__ == '__main__':
    turtle.speed(4)
    turtle.shape('turtle')
    # draw_s()
    # turtle.clear()
    # draw_square(100)
    # turtle.clear()
    # draw_circle()
    # turtle.clear()
    # draw_many_square(10, 10)
    # turtle.clear()
    # draw_spider()
    # turtle.clear()
    # draw_square_spiral()
    # turtle.clear()
    draw_spiral()
    # draw_sun()
