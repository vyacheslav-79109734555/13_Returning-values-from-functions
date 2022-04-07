a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

i = max(a, b)

if c < i:
    x = i
else:
    x = c
print(f'Максимальное число из введенных = {int(x)}')

