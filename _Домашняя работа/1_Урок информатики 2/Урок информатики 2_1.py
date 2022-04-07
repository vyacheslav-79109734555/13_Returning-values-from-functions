def count(i, n, x):
    if n != 0:
        i = int(i)
        n = round(n, x)
        print('x =', n, '* 10 **', i)
        print('или')
        print('x =', str(n) + 'e' + str(i))
    else:
        print('Работа завершена')


n = float(input('Введите число: '))
x = int(len(str(n))) - 1
# print('длина строки', x + 1)
x = len(str(n))
i = 0
if 1 < n < 10:
    n = n
    i = 0
elif 0 < n < 1:
    while n < 1:
        n = n * 10
        i += 1
elif n > 10:
    while n > 10:
        n = n / 10
        i += 1
elif -1 > n > -10:
    n = n
    i = 0
elif n > -1 and n != 0:
    while n > -1:
        n = n * 10
        i -= 1
else:
    while n < -10:
        n = n / 10
        i += 1

count(i, n, x)

