# Простые числа
a, b = 2, 15

for i in range(a, b + 1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag and i != 1:
        print(i)
