print('Задача 6. Сумма факториалов')

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N!

n = int(input("Введите число N: "))
fuct = 1
sum_fuct = 0
for row in range(1, n + 1):
    for col in range(1, row + 1) :
        fuct *= col
    sum_fuct += fuct
    fuct = 1
print("Сумма факториалов равна:", sum_fuct)
