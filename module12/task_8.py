print('Задача 8. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел

import math

def get_nod(a, b):
    nod = math.gcd(a, b)
    print("Наибольший общий делитель равен:", nod)


first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
get_nod(first_number, second_number)
