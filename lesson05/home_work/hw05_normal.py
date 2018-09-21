# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os

from lesson05.home_work import easy
from utils.console import bColors

print('\n====== Lesson 5. Normal ======\n')
curDir = os.getcwd()


menu = [
    'Перейти в папку',
    'Просмотреть содержимое текущей папки',
    'Удалить папку',
    'Создать папку',
]


def showStartMenu():
    print()
    counter = 1
    for x in menu:
        print('{}. {}'.format(counter, x))
        counter += 1


def printLs():
    global curDir
    for file in easy.ls(curDir):
        filePath = curDir + '/' + file
        if os.path.exists(filePath):
            if os.path.isfile(filePath):
                print(bColors.green(file))
            if os.path.isdir(filePath):
                print(bColors.bold(file + '(dir)'))


def moveToDir():
    answer = input('\nУкажите путь к папке: \n')
    global curDir
    if answer[0] != '/':
        answer = curDir + '/' + answer
    if answer[-1] == '/':
        answer = answer[0:-1]
    if os.path.isdir(answer):
        curDir = os.path.realpath(answer)


def rmDir():
    answer = input('\nУкажите путь к папке: \n')
    if os.path.isdir(answer):
        try:
            global curDir
            if answer in curDir:
                curDir = os.path.abspath(answer)
            easy.rm(answer)
            print('\nУспено удалено')
        except Exception as e:
            print(e)
    else:
        print('Ошибка при удалении')


def mkDir():
    answer = input('\nУкажите путь к папке: \n')
    if not os.path.exists(answer):
        try:
            if answer[0] != '/':
                answer = curDir + '/' + answer
            easy.mkdir(answer)
            print('\nПапка успешно создана')
        except Exception as e:
            print(e)
    else:
        print('Ошибка при создании')

def mainLoop():
    try:
        print('\nТекущая дирректория {}'.format(curDir))
        showStartMenu()
        answer = int(input('\nВариант ответа: \n'))
        if answer == 1:
            moveToDir()
            mainLoop()
        if answer == 2:
            printLs()
            mainLoop()
        if answer == 3:
            rmDir()
            mainLoop()
        if answer == 4:
            mkDir()
            mainLoop()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    mainLoop()