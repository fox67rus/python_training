# Decimal to Binary
num_10 = 128
num_2 = ''
while num_10 != 0:
    num_2 += str(num_10 % 2)
    num_10 //= 2

for i in range(1, len(num_2)+1):
    print(num_2[-i], end='')
