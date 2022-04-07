n_1 = float(input('Введите первое число: '))
n_2 = float(input('Введите второе число: '))
print()


def revers_number(number):
    # """Часть которая переворачивает число до точки"""
    x = int(number)
    n = 0
    while x > 0:
        digit = x % 10
        x = x // 10
        n = n * 10
        n = n + digit
        # """Часть которая переворачивает число после точки"""
        y = ''
    for i in reversed(str(number)):
        if i == '.':
            break
        y += i
        y = float('0.' + y)
        # """Вывод"""
        return n + y


print(f'Первое число наоборот = {revers_number(n_1)}')
print(f'Второе число наоборот = {revers_number(n_2)}')

print(f'\nСумма введённых чисел: {round(float(n_1) + float(n_2), 2)}')
print(f'Сумма чисел наоборот:  {round(revers_number(n_1) + revers_number(n_2), 2)}')
# print(f'Первое число наоборот: {revers_number(n_1)} ')
# print(f'Второе число наоборот: {revers_number(n_2)} ')
# print(f'Сумма: {revers_number(n_1) + revers_number(n_2)} ')

