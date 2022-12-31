# генератор списков
# new_list = [expression for member in iterable]

# # поиск четных чисел - стандартный метод
# source = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# result = []
#
# for s in source:
#     if s % 2 == 0:
#         result.append(s)
#
# print(result)

# # поиск четных чисел с помощью генератора
# result = [s for s in source if s % 2 == 0]
# print(result)

# # перебор списка кортежей
# source = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# result = []
#
# for col_sources in source:
#     for el_sources in col_sources:
#         result.append(el_sources)
#
# print(result)

# # с помощью list comprehension
# result = [el_sources for col_sources in source for el_sources in col_sources]
# print(result)

# замена отрицательных элементов на 0
source = [30, 15, -5, 7, 15, -9, ]

result = [s if s > 0 else 0 for s in source]
print(result)
