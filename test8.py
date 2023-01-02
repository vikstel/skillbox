people = int(input("Введите количество человек: "))
number = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {number}-й человек")
circle_people = list(range(1, people + 1))
print(f"Текущий круг людей: {circle_people}")
print(f"Начало счета с номера {circle_people[0]}")



