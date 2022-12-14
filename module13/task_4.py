print('Задача 4. Урок информатики 3')

# Наконец-то учитель смог объяснить детям,
# что такое эта «плавающая точка». Однако долго его радость не продлилась, 
# ведь на следующем уроке нужно будет объяснить такие страшные слова, 
# как «экспоненциальное», «мантисса» и «порядок».
 
# Хоть старшеклассники и знакомы с экспонентой,
# учитель всё равно не уверен, что здесь всё будет понятно. 
# Поэтому для наглядности он также написал программу.

# На вход подаётся строка — это экспоненциальная форма числа.
# Напишите программу, 
# которая выводит отдельно мантиссу и отдельно порядок этого числа.

def get_mant(n):
    mant = ""
    for symb in n:
        if symb == "e":
            break
        else:
            mant += symb
    return mant


def get_order(n):
    order = ""
    for i in range(len(n) - 1, -1, -1):
        if n[i] == "e":
            break
        else:
            order = n[i] + order
    return order

number = input("Введите число: ")
left = get_mant(number)
right = get_order(number)
print(f"Мантисса числа {number} - {left}, порядок числа {number} - {right}")