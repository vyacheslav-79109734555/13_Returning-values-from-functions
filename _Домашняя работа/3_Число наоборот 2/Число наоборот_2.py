while True:
    numb_1 = input('Введите первое число: ')
    numb_2 = input('Введите второе число: ')
    if numb_1.isdigit() and numb_2.isdigit():
        print('ok')
        break
    print('Упс что пошло не так, попробуй еще раз: ')


def revers_number(number):
    x = int(number)
    a = int(len(number))
    n = 0

    for i in range(a):
        result = x % 10
        x = x // 10
        n = n * 10
        n = n + result
    return n


print(f'\nПервое число наоборот = {revers_number(numb_1)}')
print(f'Второе число наоборот = {revers_number(numb_2)}')
print(f'\nСумма введённых чисел: {int(numb_1) + int(numb_2)}')
print(f'Сумма чисел наоборот: {revers_number(numb_1) + revers_number(numb_2)}')

