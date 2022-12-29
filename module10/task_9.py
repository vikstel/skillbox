print('Задача 9. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

height = int(input("Введите высоту пирамиды: "))
number = 1
for line in range(height):
    space_count = height - line - 1
    print("   " * space_count, end="")
    for num in range(line + 1):
        print(number, end="    ")
        number += 2
    print()

