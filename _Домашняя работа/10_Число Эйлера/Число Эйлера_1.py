import math as m

accuracy = float(input('Точность: '))

e = 0
n = 0
num = 1

while num > accuracy:
    num = 1 / m.factorial(n)
    e += num
    n += 1

print(f'Результат: {e}')
