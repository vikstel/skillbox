print('Задача 7. Опять?')

# Вы снова встретились со своим старым другом, 
# который был безмерно благодарен вам за то,
# что вы помогли ему сдать задачу тому преподавателю.
# 
# Вот только друг всё равно выглядел довольно грустным. 
# Спросив в чём дело, друг взорвался эмоциями и рассказал,
# что теперь препод попросил написать функцию нахождения минимального числа
# без использования условного оператора, циклов и функции min. 
# 
# Конечно же, вы решили снова помочь бедняге.
# Напишите для него такую программу.

def get_min(a, b):
    min_number = (a + b - abs(a - b)) // 2
    print("Минимальное число равно:", min_number)


first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
get_min(first_number, second_number)