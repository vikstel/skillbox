print('Задача 7. Стипендия')

#Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
# 
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.

educational_grant = int(input("Введите сумму стипендии в иесяц: "))
expenses = int(input("Введите сумму расходов в месяц: "))
parents_help = 0
debet = 0
for month in range(10):
    debet = expenses - educational_grant
    parents_help += debet
    expenses *= 1.03

print(int(parents_help))




