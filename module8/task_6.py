print('Задача 6. Письмо')

# У нас есть
# квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги,
# которое не помещается в конверт.
# 
# Напишите программу,
# которая подскажет сколько раз нужно сложить письмо пополам,
# чтобы оно поместилось в конверт.
# Размеры письма вводятся с клавиатуры.

box_size = 12
letter_length = int(input("Введите длину письма: "))
letter_width = int(input("Введите ширину письма: "))
count = 0
thrase = ""
if letter_width <= box_size and letter_length <= box_size:
    print("Письмо помещается в конверт.")
else:
    while letter_length > box_size or letter_width > box_size:
        if letter_length > box_size:
            letter_length /= 2
            letter_length, letter_width = letter_width, letter_length
        elif letter_width > box_size:
            letter_width /= 2
            letter_length, letter_width = letter_width, letter_length
        count += 1
    if count == 2 or count == 3 or count == 4:
        thrase = "раза"
    else:
        thrase = "раз"


    print("Если письмо сложить " + str(count) + " " + str(thrase) + ", то оно поместится в конверт.")






