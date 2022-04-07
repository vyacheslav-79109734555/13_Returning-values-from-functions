a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

d = a + b
if abs(c - d) < 1e15:
    print(a)
    print(b)
    print(d)
    print(c - d)
    print('True')
else:
    print(a)
    print(b)
    print(d)
    print('False')
