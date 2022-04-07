def revers(n):
    numbers = ''
    while n != 0:
        numbers += (str(n % 10))
        n //= 10
    return numbers


def revers_number(num_a, num_b):
    num_a = revers(num_a)
    num_b = revers(num_b)
    print(f'\nПервое число наоборот = {num_a}')
    print(f'Второе число наоборот = {num_b}')
    summa = int(num_a) + int(num_b)
    print(f'\nСумма введённых чисел = {summa}')
    s = revers(summa)
    print(f'Сумма чисел наоборот = {s}')


numb_1 = int(input('Введите первое число: '))
numb_2 = int(input('Введите второе число: '))

revers_number(numb_1, numb_2)

