import re

__author__ = 'Переверза Дмитрий Витальевич'

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def fractionalOperations(fractionals):
    """
    Операции (сложение и вычитание) с простыми дробями.
    >>> fractionalOperations('5/6 + 4/7')
    Ответ: 1 17/42
    >>> fractionalOperations('-2/3 - -2')
    Ответ: 1 1/3
    >>> fractionalOperations('5/6 + 4/7')
    Ответ: 1 17/42
    """
    # Парсим входную строку
    result = re.search(r"(\-?[\d\s\/]+)(\-|\+)(.+)", fractionals)
    firstFract = result.group(1)
    operation = result.group(2)
    secondFract = result.group(3)

    from collections import namedtuple
    FractDigit = namedtuple('FractDigit', 'integer topNum downNum')
    # Парсим первое число
    result = re.search(r"(\s+?\-?\d+(?=\s|$))?((\-?\s?\d+)\/(\d+))?", firstFract)
    integer = int(result.group(1)) if result.group(1) else 0
    topNum = int(result.group(3)) if result.group(3) else 0
    downNum = int(result.group(4)) if result.group(4) else 0
    numberFirst = FractDigit(integer, topNum, downNum)
    # Парсим второе число
    result = re.search(r"(\s+?\-?\d+(?=\s|$))?((\-?\s?\d+)\/(\d+))?", secondFract)
    integer = int(result.group(1)) if result.group(1) else 0
    topNum = int(result.group(3)) if result.group(3) else 0
    downNum = int(result.group(4)) if result.group(4) else 0
    numberSecond = FractDigit(integer, topNum, downNum)

    def hideIntegerPart(num: FractDigit):
        if num.downNum:
            top = num.topNum + abs(num.integer * num.downNum)
            if num.integer:
                top = (num.integer / abs(num.integer)) * top
            return FractDigit(0, int(top), num.downNum)
        return num

    # Вынесем целые части
    numberFirst = hideIntegerPart(numberFirst)
    numberSecond = hideIntegerPart(numberSecond)


    def getNOK(a, b):
        if a == 0 or b == 0:
            return max(a, b)
        i = min(a, b)
        while True:
            if i % a == 0 and i % b == 0:
                break
            i += 1
        return i

    # Наименьшее общее кратное чисел
    nok = getNOK(numberFirst.downNum, numberSecond.downNum)

    def toNOK(num: FractDigit, nok):
        if num.downNum:
            mul = nok / num.downNum * num.topNum
        else:
            mul = nok * num.integer
        return FractDigit(0, mul, nok)

    numberFirst = toNOK(numberFirst, nok)
    numberSecond = toNOK(numberSecond, nok)

    def calculate(num_first: FractDigit, num_second: FractDigit, action):
        if action == '-':
            return FractDigit(0, int(num_first.topNum) - num_second.topNum, num_first.downNum)
        if action == '+':
            return FractDigit(0, num_first.topNum + num_second.topNum, num_first.downNum)

    resultNum = calculate(numberFirst, numberSecond, operation)

    integer = abs(resultNum.topNum) // resultNum.downNum
    top = abs(resultNum.topNum) % resultNum.downNum
    down = resultNum.downNum

    if integer:
        integer = (resultNum.topNum / abs(resultNum.topNum)) * integer
    else:
        top = (resultNum.topNum / abs(resultNum.topNum)) * top

    resultNum = FractDigit(int(integer), int(top), down)

    intString = ''
    if resultNum.integer:
        intString = str(resultNum.integer)

    if resultNum.topNum:
        fractPart = '{}/{}'.format(resultNum.topNum, resultNum.downNum)

    print("Ответ: {} {}".format(intString, fractPart))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
