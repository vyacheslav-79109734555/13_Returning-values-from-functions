while True:
    first_n = int(input("Введите первое число: "))
    num_count_1 = len(str(first_n))
    if num_count_1 > 2:
        print('ok')
        break
    else:
        print("В первом числе меньше трёх цифр.")
while True:
    second_n = int(input("Введите второе число: "))
    num_count_2 = len(str(second_n))
    if num_count_2 > 3:
        print('ok')
        break
    else:
        print("Во втором числе меньше четырёх цифр.")


def backwards_numb(numb, a):
    for i in range(a):
        last_digit = numb % 10  # последняя _ цифра
        first_digit = numb // 10 ** (a - 1)  # первая _ цифра
        between_digits = numb % 10 ** (a - 1) // 10  # между цифрами
        n = last_digit * 10 ** (a - 1) + between_digits * 10 + first_digit  # Изменённое число
    return n


print(f'Изменённое первое число = {backwards_numb(first_n, num_count_1)}')
print(f'Изменённое второе число = {backwards_numb(second_n, num_count_2)}')
print(f'Сумма чисел: {backwards_numb(first_n, num_count_1) + backwards_numb(second_n, num_count_2)}')

