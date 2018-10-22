# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os, sys

# !!! Здесь и ниже аргумент в скобках указан, потому что не получалось без этого использовать
# эти функции в нормал !!!
def make_dir(dir_name):
    if not dir_name:
        print("Необходимо указать имя папки вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print("Директория {} успешно создана".format(dir_name))
    except FileExistsError:
        print("Директория {} уже существует".format(dir_name))


if __name__ == "__main__":
    for _ in range(1, 10):
        dir_name = "dir_" + str(_)
        make_dir(dir_name)


def remove_dir(dir_name):
    if not dir_name:
        print("Необходимо указать имя папки вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print("Директория {} успешно удалена".format(dir_name))
    except FileNotFoundError:
        print("Директории {} не существует".format(dir_name))   # Здесь можно было бы написать просто continue
    except OSError:
        print("Папка не пуста")


if __name__ == "__main__":
    for _ in range(1, 10):
        dir_name = "dir_" + str(_)
        remove_dir(dir_name)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Отобразит не только директории, но и всё остальное
def list_dir():
    print("В текущей директории находится: ", os.listdir(os.getcwd()))


def list_dirs():
    list_ = ""
    for dir in os.listdir(os.getcwd()):
        if os.path.isdir(dir):
            list_ += str(dir) + "; "
    if list_ != "":
        print("В текущей папке находятся следующие директории: ", list_)
    else:
        print("В текущей директории нет папок.")

#list_dirs()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_current_file():
    src = os.path.join(os.getcwd(), os.path.basename(__file__))
    dst = os.path.join(os.getcwd(), 'copy_' + os.path.basename(__file__))

    source = open(src, 'r', encoding="UTF-8")
    dest = open(dst, 'w', encoding="UTF-8")

    while True:
        copy_buffer = source.read()
        if not copy_buffer:
            break
        dest.write(copy_buffer)
        print(copy_buffer)

    source.close()
    dest.close()

#copy_current_file()
