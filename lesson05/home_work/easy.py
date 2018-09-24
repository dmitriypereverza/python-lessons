import os
import shutil


def mkdir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

def rm(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)

def ls(path):
    return os.listdir(path)

def copy(path, new_name):
    if os.path.isfile(path):
        shutil.copyfile(path, new_name)
    if os.path.isdir(path):
        shutil.copytree(path, new_name)