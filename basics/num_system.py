def num_sys10(num: int, base=8):
    """ перевод из десятичной СС в любую другую от 2-ной до 9-ной
        num - конвертируемое целое число
        base - основание системы счисления
    """
    if base <= 1 or base > 10 or num < 0:
        return "Error: ~"
    new_num = ""
    while num > 0:
        new_num = new_num + str(num % base)
        num //= base
    return new_num[::-1]


if __name__ == '__main__':
    print(num_sys10(10))
