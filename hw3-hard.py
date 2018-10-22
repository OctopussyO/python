# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
print("***Задача №1***")

def nod(list_):
    a = list_[0]
    for i in range(1, len(list_)):
        if a != 1:            
            b = list_[i]
            if b != 1:
                while b:
                    a, b = b, a%b                
            else:
                a = list_[i]
                continue
        else:
            a = list_[i]
            continue
    NOD = abs(a)
    return NOD
    
def nok(list_, NOD):
    pr = 1
    for i in range(len(list_)):
        pr = pr * list_[i]
    NOK = pr / NOD
    return NOK

x = (input("Введите выражение: ")).split(" ")

cis = []
zn = []
s = []

if "+" not in x[0]:
    s.append(1)
elif "-" in x[0]:
    s.append(-1)
    x = x[1:]

i = 0
while len(x) > 0:
    if "/" in x[i]:
        cis.append(int(x[i].split("/")[0]))
        zn.append(int(x[i].split("/")[1]))
    elif x[i] == "+":
        s.append(1)
    elif x[i] == "-":
        s.append(-1)
    else:
        cis.append(int(x[i]))
        zn.append(1)
        s.append(1)
    x = x[i+1:]

NOK = nok(zn, nod(zn))

c = 0
z = int(NOK)
cel = ""

for i in range(len(cis)):
    c = c + s[i] * cis[i] * NOK / zn[i]

NOD = nod([c, NOK])

c = int(c / NOD)
z = int(z / NOD)

if abs(c // z) >= 1:
    cel = int(c // z)
    c = int(abs(c % z))

print("Результат вычисления: {} {}/{}".format(cel, c, z))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

print("\n***Задача №2***")

import os

def read_file(file_):
    list_ = []
    rab = []
    a = []
    for line in file_:    
        a = line.lstrip("\ufeff").rstrip("\n")
        rab = []
        while len(a) > 0:
            if a.count(" ") > 0:
                rab.append(a[:a.index(" ")])
                a = a[a.index(" "):].lstrip(" ")
            elif a.count(" ") == 0:
                rab.append(a)
                a = a.lstrip(a)
        list_.append(tuple(rab))
    return tuple(list_)

path = os.path.join('data', 'workers.txt')
f_workers = open(path, 'r', encoding='UTF-8')

workers = read_file(f_workers)

f_workers.close()


path = os.path.join('data', 'hours_of.txt')
f_ved = open(path, 'r', encoding='UTF-8')

ved = read_file(f_ved)

f_ved.close()


cash = ["Итог"]
for j in range(1, len(ved)):
    for i in range(1, len(workers)):
        if ved[j][0] == workers[i][0] and ved[j][1] == workers[i][1]:
            time = int(ved[j][2])
            time_n = int(workers[i][4])
            oklad = int(workers[i][2])
            if time == time_n:
                zp = round(oklad, 2)
            elif time < time_n:
                zp = round((oklad * time / time_n), 2)
            elif time > time_n:
                zp = round((oklad + (1 + (time - time_n) / time_n) * 2), 2)
            cash.append(zp) # Решила оставить этот список для красоты, хотя принтить можно было и отсюда.

print("Заработная плата работников составит:\n")
for j in range(len(ved)):
    print("{:<9}{:<10}{:<7}".format(ved[j][0], ved[j][1], cash[j]))

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

print("\n***Задача №3***")
import os

def read_file(file_):
    list_ = []
    a = []
    for line in file_:
        a = line.lstrip("\ufeff").rstrip("\n")
        if bool(a) == True:
            list_.append(a)
        else:
            continue
    return tuple(list_)

path = os.path.join('data', 'fruits.txt')
f_fruits = open(path, 'r', encoding='UTF-8')

fruits = read_file(f_fruits)

f_fruits.close()


alphabet = tuple(map(chr, range(ord('А'), ord('Я')+1)))

for i in range(len(fruits)):
    for j in range(len(alphabet)):
        if fruits[i][0] == alphabet[j]:
            path = os.path.join('data', 'fruits', 'file_'+alphabet[j]+'.txt')
            file = open(path, 'a')
            file.write(fruits[i]+'\n')
            file.close()
