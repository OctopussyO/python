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

import os, sys, shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("ping - тестовый ключ")
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> - создать копию файла")
    print("rm <file_name> - удалить файл")
    print("cd <full_path or relative_path> - сменить текущую директорию на указанную")
    print("ls - показать полный путь текущей директории")


def ping():
    print("pong")


def make_dir():
    if not param:
        print("Необходимо указать имя папки вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), param)
    try:
        os.mkdir(dir_path)
        print("Директория {} успешно создана".format(param))
    except FileExistsError:
        print("Директория {} уже существует".format(param))


def copy_file():
    if not param:
        print("Необходимо указать имя файла вторым параметром")
        return
    src = os.path.join(os.getcwd(), param)
    dst = os.path.join(os.getcwd(), 'copy_' + param)
    try:
        shutil.copy(src, dst)
        print("Файл успешно скопирован - copy_{}".format(param))
    except IOError:
        print("Не удалось скопировать файл")


def remove_file():
    path = os.path.join(os.getcwd(), param)
    access = input("Вы уверены, что хотите удалить файл? (Y/N)")
    if os.path.isfile(path) and access == 'Y':
        os.remove(path)
        print("Файл удален")
    elif os.path.isfile(path) == False and access == 'Y':
        print("Файл не найден")


def change_dir():
    if not param:
        print("Необходимо указать директорию")
        return
    try:
        os.chdir(param)
        print("Успешно перешел:", os.getcwd())
    except FileNotFoundError:
        dir_path = os.path.join(os.getcwd(), param)
        try:
            os.chdir(dir_path)
            print("Успешно перешел:", os.getcwd())
        except FileNotFoundError:
            print('Невозможно перейти')


def get_cwd():
    print(os.getcwd())


do = {
    "ping": ping,
    "help": print_help,
    "mkdir": make_dir,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": get_cwd,
    }

try:
    param = sys.argv[2]
except IndexError:
    param = None
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
