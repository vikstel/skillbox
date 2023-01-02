guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]
while True:
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
    question = input("Гость пришёл или ушёл? ")
    if question == "Пора спать":
        print("Вечеринка закончилась, все легли спать.")
        break
    elif question == "пришёл" or question == "пришел":
        name = input("Имя гостя: ")
        if len(guests) <= 5:
            print(f"Привет, {name}!")
            guests.append(name)
        else:
            print(f"Прости, {name}, но мест нет.")
    elif question == "ушёл" or question == "ушел":
        name = input("Имя гостя: ")
        print(f"Пока, {name}!")
        guests.remove(name)


