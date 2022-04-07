def factorial_n(num):
    factorial = 1
    for n in range(1, num + 1):
        factorial *= n
    return factorial


def degree_n(x, n):
    count = x
    for n in range(n - 1):
        count *= x
    return count


def search(x, precIsion):
    temp = 1
    result = 1
    n = 1
    while abs(temp) > precIsion:
        temp = degree_n(-1, n) * (degree_n(x, (2 * n)) / factorial_n(2 * n))
        result += temp
        n += 1
    return result


while True:
    try:
        precision = float(input('Введите точность вычисления: '))
        numb_x = float(input('Введите действительное число "х" '))
        print(f'Сумма ряда = {search(numb_x, precision)}')
    except ValueError:
        print('Введите корректные данные!')
