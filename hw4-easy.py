# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
print("***Задача №1***")

new1 = [int(el) ** 2 for el in input("Введите произвольные целые числа через "\
                                     "пробел: ").split(" ")]
print("Я возвёл их в квадрат: ", new1)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
print("\n***Задача №2***")

# a = input("Введите первый список фруктов через пробел: ").split(" ")
# b = input("Введите второй список фруктов через пробел: ").split(" ")

a = ['банан', 'яблоко', 'тыква', 'картошка', 'груша', 'персик']
b = ['персик', 'морковь', 'тыква', 'мандарин', 'клюква', 'арбуз', 'киви']

new2 = [ela for ela in a for elb in b if ela == elb]

print("Первый список: {}\nВторой список: {}\nФрукты, присутствующие в обоих "\
      "списках: {}".format(a, b, new2))

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
print("\n***Задача №3***")

import random

list_ = [random.randint(-100, 100) for _ in range(int(input("Введите желаемую "\
                                                            "длину списка: ")))]
print("Я сделал список произвольных чисел: ", list_)

new3 = [el for el in list_ if el % 3 == 0 and el > 0 and el % 4 != 0]
print("А это - список, удовлетворяющий условиям задачи: ", new3)
