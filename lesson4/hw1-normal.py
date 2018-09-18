import re

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
from random import randint


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


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

print("\nПервое задание")

resultList = re.findall(r"((?<=[A-Z])|^)([a-z]+)((?=[A-Z]{1,})|$)", line)
resultList = list(map(lambda x: x[1], resultList))
result = re.sub(r"((?<=[A-Z])|^)([a-z]+)((?=[A-Z]{1,})|$)", r"{}\2{}".format(bcolors.OKGREEN, bcolors.ENDC), line)
print("Способ c re:\t {}".format(result))
print("Способ c re:\t {}".format(resultList))

resultList = []
resultStrings = ''
currentString = ''
for char in line:
    if char.isupper():
        if len(currentString):
            resultStrings += r"{}{}{}".format(bcolors.OKGREEN, currentString, bcolors.ENDC)
            resultList.append(currentString)
            currentString = ''
            resultStrings += char
        else:
            resultStrings += char
        continue
    currentString += char

print("Способ без re:\t {}".format(resultStrings))
print("Способ без re:\t {}".format(resultList))

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

print("\nВторое задание")

result = re.sub(r"(?<=[a-z]{2})([A-Z]+)(?=[A-Z]{2})", r"{}\1{}".format(bcolors.OKGREEN, bcolors.ENDC), line_2)
print("Способ c re:\t {}".format(result))

resultList = re.findall(r"(?<=[a-z]{2})([A-Z]+)(?=[A-Z]{2})", line_2)
resultList = list(map(lambda x: x, resultList))
print("Способ c re:\t {}".format(resultList))

resultList = []
resultStrings = ''
beforeLower = ''
afterUpper = ''
for char in line_2:
    if char.islower():
        if len(beforeLower) >= 2 and len(afterUpper) > 2:
            resultStrings += r"{}{}{}{}{}".format(beforeLower, bcolors.OKGREEN, afterUpper[:-2], bcolors.ENDC,
                                                  afterUpper[-2:])
            resultList.append(afterUpper[:-2])
            afterUpper = ''
            beforeLower = ''
        if len(afterUpper):
            resultStrings += beforeLower + afterUpper
            afterUpper = ''
            beforeLower = ''
        beforeLower += char.lower()
    elif char.isupper():
        if len(beforeLower) >= 2:
            afterUpper += char
            continue
        resultStrings += beforeLower + char
        currentString = ''
        afterUpper = ''
        beforeLower = ''

print("Способ без re:\t {}".format(resultStrings))
print("Способ без re:\t {}".format(resultList))

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.


with open('data/longnum.txt', 'w', encoding='utf-8') as f:
    num = ''.join([str(randint(0, 9)) for _ in range(2500)])
    num.join(str(randint(1, 9)))
    f.write(num)

digitsSeq = ['?']
with open('data/longnum.txt', 'r', encoding='utf-8') as f:
    longNumber = f.readline()
    foundList = re.findall(r'([0]{2,}|[1]{2,}|[2]{2,}|[3]{2,}|[4]{2,}|' \
                           '[5]{2,}|[6]{2,}|[7]{2,}|[8]{2,}|[9]{2,})', longNumber)
    [digitsSeq.insert(0, x) for x in foundList if len(x) > len(digitsSeq[0])]

print('Самое длинное число в файле: {}'.format(digitsSeq[0]))