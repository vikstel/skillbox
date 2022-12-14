

cube_player = int(input("Кубик Кости: "))
cube_owner = int(input("Кубик  владельца: "))
if cube_player >= cube_owner:
    result = cube_player - cube_owner
    print("Разность: " + str(result))
    print("Игрок платит")
else:
    result = cube_player + cube_owner
    print("Сумма: " + str(result))
    print("Владелец платит")
print("Игра окончена")
