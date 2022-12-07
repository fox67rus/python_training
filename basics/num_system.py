# перевод из десятичной СС в любую другую

base = 8
num = int(input("Input some number: "))

while num > 0:
    new_num = num % base
    print(new_num, end="")
    num //= base
