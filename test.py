def len_number(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


def correct_age():
    age = int(input("Введите возраст: "))
    while age <= 0:
        age = int(input("Введите возраст: "))
    return age

def get_index():
    n = input("Введите индекс: ")
    index = ''
    for symb in str(n):
        if "0" <= symb <= "9":
            index += symb
    return int(index)




def get_count_digit(n):
    number = int(input())
    while len_number(number) != n:
        number = int(input("Попробуйте еще раз: "))
    return number

print("Введите ОГРНИП (15 цифр): ", end="")
ogrnyp = get_ogrnyp(15)
print(ogrnyp)







