def count_n(numb):
    count = 0
    for i in range(1, numb + 1):
        count += i
    return count


first_n = int(input('Введите число: '))

second_n = count_n(first_n)

n_first_value = count_n(first_n)
n_second_value = count_n(second_n)

print(f'Сумма от 1 до {first_n} = {n_first_value}')
print(f'Сумма от 1 до {second_n} = {n_second_value}')
