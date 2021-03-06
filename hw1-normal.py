__author__ = 'Дорошина Юлия Павловна'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

print("***Задача 1***")

number = int(input("Введите целое число: "))
max = 0
num = number

while number > 0:
    num = number % 10
    number = number // 10
    if num > max:
        max = num
        
print("Максимальная цифра в этом числе - ", max, sep = '')

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

print("\n***Задача 2***")

a = input("Введите значение переменной A: ")
b = input("Введите значение переменной B: ")

a = a + b
b = a[0:len(a)-len(b)]
a = a[len(b):len(a)]

print("Я поменял их местами :)\nA = ", a, "\nB = ", b, sep = '')

a, b = b, a

print("Я поменял их обратно другим способом :)\nA = ", a, "\nB = ", b, sep = '')

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print("\n***Задача 3***")

import math

print("Имеется уравнение вида: ax² + bx + c = 0\nВведите значения коэффициентов:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b**2 - 4 * a * c

if D >= 0:
    x1 = (- b + math.sqrt(D)) / (2 * a)
    x2 = (- b - math.sqrt(D)) / (2 * a)
    print("Корни уравнения:", "\nx1 = ", x1, "\nx2 = ", x2, sep = "")
else:
    print("Корни уравнения - комплексные числа")
