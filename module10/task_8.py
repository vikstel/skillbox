print('Задача 8. Пирамидка')


# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.


# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

   #
  ###
 #####
#######

n = int(input("Введите высоту пирамиды: "))
space = 1
for line in range(n):
    print(" " * (5 - line - 2), end="")
    print("#" * space)
    space += 2

