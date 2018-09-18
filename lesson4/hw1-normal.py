import os
import re
import random

from utils.console import bColors

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO' \
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK' \
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn' \
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa' \
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete' \
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ' \
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb' \
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC' \
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB' \
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT' \
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu' \
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB' \
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa' \
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ' \
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

print(bColors.bold("\nПервое задание"))

def get_matches_first_task(line):
    """
    >>> get_matches_first_task('sGAMkgAYEOmHBSQsSUHKvS')
    ['s', 'kg', 'm', 's', 'v']
    >>> get_matches_first_task('mtMmEZUOmcqWiryMQhhTxqKdSTKCYE')
    ['mt', 'm', 'mcq', 'iry', 'hh', 'xq', 'd']
    """
    resultList = re.findall(r"((?<=[A-Z])|^)([a-z]+)((?=[A-Z]{1,})|$)", line)
    return list(map(lambda x: x[1], resultList))

def get_matches_first_task_without_re(line):
    """
    >>> get_matches_first_task_without_re('sGAMkgAYEOmHBSQsSUHKvS')
    ['s', 'kg', 'm', 's', 'v']
    >>> get_matches_first_task_without_re('mtMmEZUOmcqWiryMQhhTxqKdSTKCYE')
    ['mt', 'm', 'mcq', 'iry', 'hh', 'xq', 'd']
    """
    resultList = []
    currentString = ''
    for char in line:
        if char.isupper():
            if len(currentString):
                resultList.append(currentString)
                currentString = ''
            continue
        currentString += char
    return resultList

result = re.sub(r"((?<=[A-Z])|^)([a-z]+)((?=[A-Z]{1,})|$)", bColors.green(r"\2"), line)
print("Строка с выделениями: {}".format(result))
print("Способ c re:\t {}".format(get_matches_first_task(line)))
print("Способ без re:\t {}".format(get_matches_first_task_without_re(line)))

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mcqWiryMQhhTUZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm' \
         'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV' \
         'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA' \
         'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV' \
         'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW' \
         'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC' \
         'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR' \
         'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm' \
         'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn' \
         'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS' \
         'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf' \
         'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH' \
         'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN' \
         'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ' \
         'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

print(bColors.bold("\nВторое задание"))

def get_matches_second_task(line):
    """
    >>> get_matches_second_task('mcqWiryMQhhTUZUOmcqWiryMQhhTxqKdSTKCYEJlE')
    ['TUZ']
    >>> get_matches_second_task('AMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMu')
    ['AY', 'NOGI']
    >>> get_matches_second_task('GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec')
    ['AY', 'NOGI', 'P']
    """
    resultList = re.findall(r"(?<=[a-z]{2})([A-Z]+)(?=[A-Z]{2})", line)
    return list(map(lambda x: x, resultList))

def get_matches_second_task_without_re(line):
    """
    >>> get_matches_second_task_without_re('mcqWiryMQhhTUZUOmcqWiryMQhhTxqKdSTKCYEJlE')
    ['TUZ']
    >>> get_matches_second_task_without_re('AMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMu')
    ['AY', 'NOGI']
    >>> get_matches_second_task_without_re('GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec')
    ['AY', 'NOGI', 'P']
    """
    resultList = []
    beforeLower = ''
    afterUpper = ''
    for char in line:
        if char.islower():
            if len(beforeLower) >= 2 and len(afterUpper) > 2:
                resultList.append(afterUpper[:-2])
                afterUpper = ''
                beforeLower = ''
            if len(afterUpper):
                afterUpper = ''
                beforeLower = ''
            beforeLower += char.lower()
        elif char.isupper():
            if len(beforeLower) >= 2:
                afterUpper += char
                continue
            afterUpper = ''
            beforeLower = ''
    return resultList


result = re.sub(r"(?<=[a-z]{2})([A-Z]+)(?=[A-Z]{2})", bColors.green(r"\1"), line_2)
print("Строка с выделениями: {}".format(result))
print("Способ c re:\t {}".format(get_matches_second_task(line_2)))
print("Способ без re:\t {}".format(get_matches_second_task_without_re(line_2)))


# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

print(bColors.bold("\nТретье задание"))

def get_long_seq(long_string_num):
    """
    >>> get_long_seq('33456564511153564')
    '111'
    >>> get_long_seq('3345656451115399994')
    '9999'
    >>> get_long_seq('3345656000004511153564')
    '00000'
    """
    digitsSeq = ['?']
    foundList = re.findall(r'([0]{2,}|[1]{2,}|[2]{2,}|[3]{2,}|[4]{2,}|' \
                               '[5]{2,}|[6]{2,}|[7]{2,}|[8]{2,}|[9]{2,})', long_string_num)
    [digitsSeq.insert(0, x) for x in foundList if len(x) > len(digitsSeq[0])]
    return digitsSeq[0]

file = os.path.realpath('data/longnum.txt')
with open(file, 'w', encoding='utf-8') as f:
    num = ''.join([str(random.randint(0, 9)) for _ in range(2500)])
    num.join(str(random.randint(1, 9)))
    f.write(num)
with open(file, 'r', encoding='utf-8') as f:
    longNumber = f.readline()
print('Самое длинное число в файле {}: {}'.format(file, get_long_seq(longNumber)))

if __name__ == "__main__":
    import doctest
    doctest.testmod()