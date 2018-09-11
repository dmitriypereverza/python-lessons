from math import sqrt
from random import randint

__author__ = 'Переверза Дмитрий Витальевич'

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

list = []
elem = True
while elem:
    elem = input("Добавьте элемент списка:\n")
    if not elem.isnumeric():
        elem = False
        continue
    list.append(int(elem))
    print(list)

print('Исходный список: {}'.format(list))
results = [int(sqrt(x)) for x in list if x > 0 and not sqrt(x)%1]
print('Результат: {}'.format(results))

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

days_name_list = [
    'первое',
    'второе',
    'третье',
    'четвертое',
    'пятое',
    'шестое',
    'седьмое',
    'восьмое',
    'девятое',
]
dozen_10_list = [
    'одиннадцатое',
    'двенадцатое',
    'тринадцатое',
    'четырнадцатое',
    'пятнадцатое',
    'шестнадцатое',
    'семнадцатое',
    'восемнадцатое',
    'девятнадцатое',
]
month_name_list = [
    'января',
    'февраля',
    'марта',
    'апреля',
    'мая',
    'июня',
    'июля',
    'август',
    'сентября',
    'октября',
    'ноября',
    'декабря',
]
dozens_name_list = [
    ('десятое', 'десятое'),
    ('двадцать', 'двадцатое'),
    ('тридцать', 'тридцатое'),
]
date = input('Введите дату в формате dd.mm.yyyy:')
if len(date) != 10:
    raise AttributeError('Неверный формат даты')
day = date[0:2]
month = date[3:5]
year = date[6:10]
if not day.isnumeric() or not 0 < int(day) <= 31:
    raise ArithmeticError('Неверно введен день')
if not month.isnumeric() or not 0 < int(month) <= 12:
    raise AttributeError('Неверно введен мясяц')
if not year.isnumeric() or not 0 < int(year):
    raise AttributeError('Неверно введен год')
day = int(day)
month = int(month)
year = int(year)

month_name = month_name_list[month - 1]
days_name = ''
if day < 10:
    days_name = days_name_list[day - 1]
elif 20 > day > 10:
    days_name = dozen_10_list[day%10 - 1]
elif day >= 20 or day == 10:
    dozen = day // 10
    dozens_name = dozens_name_list[dozen - 1]
    if day % 10:
        days_name = '{} {}'.format(dozens_name_list[dozen - 1][0], days_name_list[day%10 - 1])
    else:
        days_name = dozens_name_list[dozen - 1][1]

print('Вы ввели: {} {} {} года'.format(days_name, month_name, year))


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

while True:
    n = input("Cколько случайных чисел нужно сгенерировать: \n")
    if n.isnumeric():
        break
    print('Вы ввели не число. Попробуйте еще раз')

result_list = [randint(-100, 100) for _ in range(int(n))]
print(result_list)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

data = []
while True:
    elem = input("Добавьте элемент списка:\n")
    if not elem:
        break
    if not elem.isnumeric():
        print('Введите число!')
    data.append(int(elem))
    print(data)
print('Сгенерированный список: {}'.format(data))
print('a) Неповторяющиеся элементы исходного списка: {}'.format(list(set(data))))
uniqs = list(set(data))
for i in uniqs:
    data.remove(i)
more_list = list(set(uniqs) - set(data))
print('б) Элементы исходного списка, которые не имеют повторений: {}'.format(more_list))
