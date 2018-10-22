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
import sys
from hw5_easy import list_dir, make_dir, remove_dir

print('sys.argv = ', sys.argv)

def print_help():
    print("Выберите действие:")
    print("1 - перейти в папку")
    print("2 - содержимое текущей папки")
    print("3 - удалить папку")
    print("4 - создать папку")
    print("help - список команд")
    print("end - закончить")


def change_dir(dir_name):
    try:
        os.chdir(dir_name)
        print("Успешно перешел")
    except FileNotFoundError:
        print('Невозможно перейти')


print_help()

i = 0
while True:
    choise = input()

    if choise == '1':
        change_dir(input("Введите имя папки: "))
    elif choise == '2':
        print(os.listdir(os.getcwd()))
    elif choise == '3':
        remove_dir(input("Введите имя папки: "))
    elif choise == '4':
        make_dir(input("Введите имя папки: "))
    elif choise == 'help':
        print_help()
    elif choise == 'exit':
        break
    else:
        print("Неверная команда\nВведите help для справки")
