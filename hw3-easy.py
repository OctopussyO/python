__author__ = 'Дорошина Юлия Павловна'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

print("***Задача №1***")

def my_round(number, ndigits):
    x = number * (10 ** (ndigits + 1))
    if x % 10 >= 5:
        number = (x - (x % 10) + 10) / (10 ** (ndigits + 1))
    else:
        number = (x - (x % 10)) / (10 ** (ndigits + 1))
    return number

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

print("\n***Задача №2***")

def lucky_ticket(ticket_number):
    tn1 = ticket_number // 1000 
    tn2 = ticket_number % 1000 
    sum1=0
    sum2=0
    length = len(str(ticket_number))
    if length == 6:
        for i in range(3):
            sum1 = sum1 + tn1 % 10
            tn1 = tn1 // 10 
            sum2 = sum2 + tn2 % 10
            tn2 = tn2 // 10
    if sum1 == sum2 and length == 6:
        res = "Поздравляю! У Вас счастливый билет!"
    else:
        res = "Это самый обычный билет."
    return res

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))


