# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os
print([dir for dir in os.listdir('.') if os.path.isdir(dir)])