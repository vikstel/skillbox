first_lst = []
second_lst = []
for i in range(3):
    first_num = int(input(f"Введите {i + 1}-е число для первого списка: "))
    first_lst.append(first_num)
for j in range(7):
    second_num = int(input(f"Введите {j + 1}-е число для второго списка: "))
    second_lst.append(second_num)
print("Первый список:", first_lst)
print("Второй список:", second_lst)
first_lst.extend(second_lst)
for num in first_lst:
    num_count = first_lst.count(num)
    while num_count > 1:
        first_lst.remove(num)
        num_count -= 1
print("Новый первый список с уникальными элементами:", first_lst)



