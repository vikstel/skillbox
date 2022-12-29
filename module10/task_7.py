print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

n = int(input("Сколько чисел вы хотите ввести? "))
number_sum = 0
result_number_sum = 0
result_number = 0
for row in range(1, n + 1):
    print("Введите", row, "- е число: ", end="")
    number = int(input())
    time_number = number
    while number != 0:
        last_number = number % 10
        number_sum += last_number
        number //= 10
    if number_sum > result_number_sum:
        result_number_sum = number_sum
        result_number = time_number
        number_sum = 0

    else:
        number_sum = 0

print("У числа", result_number, "сумма цифр равна", result_number_sum)
