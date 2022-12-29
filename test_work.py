print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')
sep = "-" * 50
name = ""
age = ""
phone = ""
email = ""
post_index = ""
post_adress = ""
other_info = ""
ogrnyp = ""
inn = ""
payment_account = ""
bank_name = ""
bik = ""
cor_account = ""

def get_main_menu():
    print(sep)
    print("ГЛАВНОЕ МЕНЮ")
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')
    option = input('Введите номер пункта меню: ')
    if option == "0":
        print("До встречи.")
    elif option == "1":
        input_info()
    elif option == "2":
        output_info()
    else:
        print('Введите корректный пункт меню')
        get_main_menu()


def input_info():
    print(sep)
    print("ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ")
    print('1 - Личная информация')
    print('2 - Информация о предпринимателе')
    print('0 - Назад')
    option = input("Введите номер пункта меню: ")
    if option == "0":
        get_main_menu()
    elif option == "1":
        user_info()
    elif option == "2":
        business_info()
    else:
        print('Введите корректный пункт меню')
        input_info()


def user_info():
    global name
    global age
    global phone
    global email
    global post_index
    global post_adress
    global other_info
    name = input("Введите имя: ")
    age = correct_age()
    phone = input("Введите номер телефона (+7ХХХХХХХХХХ): ")
    email = input("Введите адрес электронной почты: ")
    post_index = get_index()
    post_adress = input("Введите почтовый адрес (без индекса): ")
    other_info = input("Введите дополнительную информацию: ")
    get_main_menu()


def correct_age():
    age = int(input("Введите возраст: "))
    while age <= 0:
        age = int(input("Введите возраст: "))
    return age


def len_number(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


def get_count_digit(n):
    number = int(input())
    while len_number(number) != n:
        number = int(input("Попробуйте еще раз: "))
    return number


def get_index():
    n = input("Введите индекс: ")
    index = ''
    for symb in str(n):
        if "0" <= symb <= "9":
            index += symb
    return int(index)


def business_info():
    global ogrnyp
    global inn
    global payment_account
    global bank_name
    global bik
    global cor_account
    print("Введите ОГРНИП: ", end="")
    ogrnyp = get_count_digit(15)
    inn = int(input("Введите ИНН: "))
    print("Введите расчетный счет: ", end="")
    payment_account = get_count_digit(20)
    bank_name = input("Введите название банка: ")
    bik = int(input("Введите БИК: "))
    cor_account = int(input("Введите корреспондентский счет: "))
    get_main_menu()


def output_info():
    print(sep)
    print("ВЫВЕСТИ ИНФОРМАЦИЮ")
    print('1 - Общая информация')
    print('2 - Вся информация')
    print('0 - Назад')
    option = input("Введите номер пункта меню: ")
    if option == "0":
        get_main_menu()
    elif option == "1":
        private_info()
    elif option == "2":
        all_info()
    else:
        print('Введите корректный пункт меню')
        output_info()


def private_info():
    global name
    global age
    global phone
    global email
    global post_index
    global post_adress
    global other_info
    print("Имя:", name)
    print("Возраст:", age)
    print("Телефон:", phone)
    print("E-mail:", email)
    print("Индекс:", post_index)
    print("Адрес:", post_adress)
    print("Дополнительная информация:", other_info)
    output_info()


def all_info():
    global name
    global age
    global phone
    global email
    global post_index
    global post_adress
    global other_info
    global ogrnyp
    global inn
    global payment_account
    global bank_name
    global bik
    global cor_account
    print("Имя:", name)
    print("Возраст:", age)
    print("Телефон:", phone)
    print("E-mail:", email)
    print("Индекс:", post_index)
    print("Адрес:", post_adress)
    print("Дополнительная информация:", other_info)
    print()
    print("Информация о предпринимателе")
    print("ОГРНП:", ogrnyp)
    print("ИНН:", inn)
    print("Банковские реквизиты")
    print("Р/c:", payment_account)
    print("Банк:", bank_name)
    print("БИК:", bik)
    print("К/с:", cor_account)
    output_info()


get_main_menu()