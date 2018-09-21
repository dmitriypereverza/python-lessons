# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys

sys.path.insert(0, os.path.realpath('../..'))
from utils.console import bColors
from lesson05.home_work import easy

curDir = os.getcwd()

def print_help():
    print("help - получение справки")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")
    print("mkdir <dir_name> - создание директории")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cp <file_name> - создает копию указанного файла")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def move_to_path():
    print("Текущая дирректория ", os.getcwd())
    global dir_name
    if dir_name[0] != '/':
        dir_name = curDir + '/' + dir_name
    if dir_name and os.path.exists(dir_name):
        os.chdir(dir_name)
        print("Текущая дирректория ", os.getcwd())
    else:
        print('Ошибка в пути')


def get_list():
    global dir_name
    if not dir_name:
        dir_name = curDir
    try:
        for file in easy.ls(dir_name):
            filePath = dir_name + '/' + file
            if os.path.exists(filePath):
                if os.path.isfile(filePath):
                    print(bColors.green(file))
                if os.path.isdir(filePath):
                    print(bColors.bold(file + '(dir)'))
    except FileExistsError:
        print('Ошибка при отображении файлов в {}'.format(dir_name))



def copy():
    global dir_name
    if dir_name[0] != '/':
        dir_name = curDir + '/' + dir_name
    easy.copy(dir_name, dir_name + '_copy')
    print('Успешно скопировано ' + dir_name + '_copy')


def rm():
    global dir_name
    if dir_name[0] != '/':
        dir_name = curDir + '/' + dir_name
    if os.path.exists(dir_name):
        try:
            easy.rm(dir_name)
            print('Успешно удалено ' + dir_name)
        except Exception as e:
            print('Не удалось удалить ' + dir_name)
    else:
        print('Файла не существует ' + dir_name)


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "ls": get_list,
    "rm": rm,
    "cd": move_to_path,
    "cp": copy,
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
