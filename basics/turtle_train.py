import turtle


def set_home():
    """

    """
    turtle.penup()
    turtle.home()
    turtle.pendown()


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


def draw_spiral():
    pass


def draw_square_spiral(first_side_size: int = 10, number: int = 10):
    distance = first_side_size
    for i in range(number*4):
        turtle.forward(distance)
        turtle.left(90)
        distance +=5



if __name__ == '__main__':
    turtle.speed(4)
    turtle.shape('turtle')
    # draw_s()
    # draw_square(100)
    # draw_circle()
    # draw_many_square(10, 10)
    # draw_spider()
    draw_square_spiral()
