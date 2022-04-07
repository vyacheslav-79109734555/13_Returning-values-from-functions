def counter(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

        nod = a + b
    print('НОД =', nod)


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

nod = counter(a, b)
