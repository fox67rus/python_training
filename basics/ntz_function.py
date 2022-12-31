# def summ(a, b, c=2):
#     z = (a + b) ** c
#     return z
# # result = summ(3, 5, 4)
# # print(result)

# def args(*args):
#     for a in args:
#         print(a)
#
# args(1, 2, 5, 4, 6, 8, 7, 9, 8, 7, 8, 3, 2, 4, 1000)

# def kwargs(**kwargs):
#     for k, v in kwargs.items():
#         print(f"{k} - {v}")
#
# kwargs(Alex=35, Boris=26)

# области видимости переменных
# variable = 'Global'
#
#
# def test(a, b, c, d):
#     """
#
#     :param a:
#     :param b:
#     :param c:
#     :param d:
#     """
#     variable = 'local'
#     print(variable)
#
#     def test_two():
#         global variable
#         variable = 'local 2'
#         print(variable)
#
#     test_two()
#
#
# test()
#
# print(variable)

def mul(a: int = 5, b: int = 10) -> int:
    c = a * b
    return c


x = mul(5, 6)
print(x)
