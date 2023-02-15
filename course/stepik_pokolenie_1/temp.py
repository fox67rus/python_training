# Числа Рамануджана 🌶️
# 1729 =1 ** 3 + 12 ** 3 = 9 ** 3 + 10 ** 3.

import time
start_time = time.time()
count = 0
x = 50
flag = False
for a in range(1, x):
    for b in range(1, x):
        for c in range(1, x):
            for d in range(1, x):
                sum_1 = a ** 3 + b ** 3
                sum_2 = c ** 3 + d ** 3
                if sum_1 == sum_2 and a != b and b != c and c != d and a > b and a > d and a > c:
                    count += 1
                    print(f'{a=}, {b=}, {c=}, {d=}, {sum_1=}')
                if count == 10:
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        break

print(f'Время выполнения: {time.time() - start_time}')
