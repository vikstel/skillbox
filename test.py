a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
number_5 = a.count(5)
print("Количество цифр 5 при первом объединении:", number_5)
for i in range(number_5):
    a.remove(5)
a.extend(c)
number_3 = a.count(3)
print("Количество цифр 3 при втором объединении:", number_3)
print("Итоговый список:", a)









