def max_num(num_a, num_b):
    if num_a > num_b:
        max_n = num_a
    else:
        max_n = num_b
    return max_n


a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))

x = max_num(max_num(a, b), c)

print(f'Максимальное число из введенных = {int(x)}')

