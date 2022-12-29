print('Задача 5. Простые числа')


#Напишите программу,
#которая считает количество простых чисел в заданной последовательности 
#и выводит ответ на экран.

count = int(input("Введите количество чисел: "))
number_count = 0
flag = True
for row in range(1, count + 1):
    number = int(input("Введите число: "))
    for col in range(2, number):
        if number % col == 0:
            flag = False
    if flag == True:
        number_count += 1
    else:
        flag = True
print("Количество простых чисел в последовательности:", number_count)
