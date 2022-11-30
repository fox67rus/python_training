def fibonachi(n: int) -> int:
    if n < 2:
        return n  # базовый случай
    return fibonachi(n - 1) + fibonachi(n - 2)
    # рекурсивный случай


if __name__ == '__main__':
    i = 10
    str_fib = ""
    while i > 0:
        str_fib += str(fibonachi(i))
        i -= 1
    print(str_fib[::-1])