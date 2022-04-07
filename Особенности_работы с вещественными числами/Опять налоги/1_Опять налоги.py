a = float(input('Введите бюджет страны: '))
b = float(input('Новые поступления (налог): '))
if (a + b) > a:
    print(a, '+ ', end='')
    print(b)
    print('Сумма бюджета и налогов =', a + b)
    print('Бюджет увеличится')
else:
    print(a, '+ ', end='')
    print(b)
    print('Сумма бюджета и налогов =', a + b)
    print('Результат: Бюджет не изменится')
