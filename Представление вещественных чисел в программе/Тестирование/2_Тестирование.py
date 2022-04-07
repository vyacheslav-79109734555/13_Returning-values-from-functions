x = 1
count = 0
n = float(input('Введите число в эксп.форме: '))
while x < 2:
    x = x + n
    count += 1
    print('x=', x)
print('Итераций', count)
