
__author__ = 'Переверза Дмитрий Витальевич'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    """
    Тест функции вычисления ряда фибоначи
    1,1,2,3,5
    >>> print(fibonacci(1, 3))
    [1, 1, 2]
    >>> print(fibonacci(1, 4))
    [1, 1, 2, 3]
    >>> print(fibonacci(1, 10))
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    i = 2
    fibonacciList = [1,1]
    while i <= m:
        fibonacciList.append(fibonacciList[-2] + fibonacciList[-1])
        i += 1
    return fibonacciList[n - 1:m]


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    """
    Сортировка пузырьком
    >>> print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
    [-12, -11, 0, 2, 2.5, 4, 4, 10, 20]
    >>> print(sort_to_max([-2, -10, -12, 2.5, -90]))
    [-90, -12, -10, -2, 2.5]
    """
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1
    return origin_list


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def myFilter(func, dataset):
    """
    Фильтрация массива данных
    >>> print(myFilter(lambda x: x < 0, [-1, -6, 5, 6, -1]))
    [-1, -6, -1]
    >>> print(myFilter(lambda x: x >= 3 or x == -10, range(-25, 6)))
    [-10, 3, 4, 5]
    """
    try:
        dataset_iterator = iter(dataset)
    except TypeError as te:
        print(dataset, ' is not iterable')
    if not callable(func):
        raise TypeError(func, 'is not a function')
    result = []
    for x in dataset:
        if func(x):
            result.append(x)
    return result

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def isparall(a, b, c, d):
    '''
    Проверка признаков параллелограмма
    >>> isparall((2, 3), (0, 2), (4, 1), (6, 2))
    Вершины образуют параллелограмм
    >>> isparall((2, 3), (0, 2), (4, 8), (6, 2))
    Вершины не образуют параллелограмм
    '''
    sidesEqual = False
    diagonalEqual = False
    '''
    Противополжные стороны параллельны и равны
    '''
    import math
    ab = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    cb = math.sqrt((b[0] - c[0])**2 + (b[1] - c[1])**2)
    cd = math.sqrt((d[0] - c[0])**2 + (d[1] - c[1])**2)
    ad = math.sqrt((d[0] - a[0])**2 + (d[1] - a[1])**2)
    if ab == cd and cb == ad:
        sidesEqual = True
    '''
    Диагонали O1 и O2 в точках пересечения делятся пополам и равны
    '''
    hO1 = ((a[0] + c[0])/2, (a[1] + c[1])/2)
    hO2 = ((b[0] + d[0])/2, (b[1] + d[1])/2)
    if hO1 == hO2:
        diagonalEqual = True
    if sidesEqual and diagonalEqual:
        print('Вершины образуют параллелограмм')
    else:
        print('Вершины не образуют параллелограмм')

if __name__ == "__main__":
    import doctest
    doctest.testmod()