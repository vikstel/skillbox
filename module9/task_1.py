print('Задача 1. Календарь')

# Мы продолжаем разрабатывать удобный календарь для смартфона.
# Функцию определения високосного года мы добавили,
# но забыли ещё много разных очевидных вещей.
# 
# Напишите программу,
# которая принимает от пользователя день недели в виде строки и выводит его номер на экран.
# 
# Пример:
# Введите день недели: вторник
# Номер дня недели: 2

week = ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")
day = input("Введите день недели: ")
for i, week_day in enumerate(week):
    if day == week_day:
        print("Номер дня недели:", i + 1)


