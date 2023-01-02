skates = int(input("Введите количество коньков: "))
skates_size = []
for s in range(skates):
    skate = int(input(f"Введите размер {s + 1} пары коньков: "))
    skates_size.append(skate)
people = int(input("Введите количество людей: "))
leg_size = []
for p in range(people):
    leg = int(input(f"Введите размер ноги {p + 1}-го человека: "))
    leg_size.append(leg)
count = 0
for leg in leg_size:
    if leg in skates_size:
        number = leg
        skates_size.remove(number)
        leg_size.remove(number)
        count += 1
        leg_size.insert(0, "")
print("Наибольшее кол-во людей, которые могут взять ролики:", count)


