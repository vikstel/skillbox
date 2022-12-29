print('Задача 9. Выражение')


#Дано число x.
#Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64))

x = int(input("Введите значение x: "))
s = 1
numerator = 1
denominator = 1
for i in range(6):
    s *= 2
    # print(s)
    numerator *= x - s + 1
    denominator *= x - s
if denominator == 0:
    print("Нет решения")
else:

    print(numerator / denominator)

