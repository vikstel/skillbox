def sort_class(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]

first_class = range(160, 177, 2)
second_class = range(162, 181, 3)
all_class = []
all_class.extend(first_class)
all_class.extend(second_class)

sort_class(all_class)

print(all_class)