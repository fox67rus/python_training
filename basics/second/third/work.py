#__package__ = 'basics.second.third'

from .utils import multi


def calc(a, b):
    multi("==", 10)
    print(f"a + b = {a + b}")


if __name__ == '__main__':
    calc(2, 3)
    print("In module products __package__, __name__ ==", __package__, __name__)
