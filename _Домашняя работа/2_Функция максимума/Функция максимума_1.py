def result(x):
    print(f'Максимальное число из введенных = {int(x)}')


a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

i = (a + b + abs(a - b)) / 2

if c < i:
    x = i
else:
    x = c

result(x)
