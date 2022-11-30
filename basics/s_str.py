'''
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"User's name is: {self.first_name} {self.last_name}"


user = User("John", "Doe")
print(f"{user}")
# John Doe
print(f"{user!r}")
# User's name is: John Doe



# python -m timeit -s 'x, y = "Hello", "World"' 'f"{x} {y}"'
x, y = "Hello", "World"

print(f"{x} {y}")  # 39.6 nsec per loop - Быстро!
print(x + " " + y)  # 43.5 nsec per loop
print(" ".join((x, y)))  # 58.1 nsec per loop
print("%s %s" % (x, y))  # 103 nsec per loop
print("{} {}".format(x, y))  # 141 nsec per loop

text = "hello world"

# Центрирование текста:
print(f"{text:^15}")
# '  hello world  '

number = 1234567890
# Установка разделителя групп разрядов
print(f"{number:,}")
# 1,234,567,890

number = 123
# Добавление начальных нулей
print(f"{number:08}")
# 00000123
'''


def test_assert(a, b):
    assert a == b, f"{a} ! = {b}"
    return a // b

#print(test_assert(-11, 10))
print(test_assert(-11, -11))
