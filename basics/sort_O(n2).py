def insert_sort(A):
    """ Сортировка списка А вставками """
    N = len(A)
    for top in range(1, N):
        k = top # k - текущий элемент, top - верхний элемент
        while k > 0 and A [k-1] > A[k]: # 2-е условие не проверяется, если выполняется 1-е
            A[k], A[k-1] = A[k-1], A[k]
            k -=1


def choise_sort(A):
    """ Сортировка списка А методом выбора """
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def buble_sort(A):
    """ Сортировка списка А методом пузырька """
    N = len(A)
    for bypass in range(1, N):  # количество проходов
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]


def test_sort(sort_method):
    print("Тестируем: ", sort_method.__doc__)
    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_method(A)
    print("OK" if A == A_sorted else "Fail")

    print("testcase #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))  # создание списка с помощью конкатенации двух сгенерированных
    A_sorted = list(range(20))
    sort_method(A)
    print("OK" if A == A_sorted else "Fail")

    print("testcase #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_method(A)
    print("OK" if A == A_sorted else "Fail")


if __name__ == '__main__':
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(buble_sort)
