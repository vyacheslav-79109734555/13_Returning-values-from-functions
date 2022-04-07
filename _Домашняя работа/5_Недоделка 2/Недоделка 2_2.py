def backwards_numb(numb, a):
    global revers_number
    for i in range(a):
        last_digit = numb % 10  # последняя _ цифра
        first_digit = numb // 10 ** (a - 1)  # первая _ цифра
        between_digits = numb % 10 ** (a - 1) // 10  # между цифрами
        revers_number = last_digit * 10 ** (a - 1) + between_digits * 10 + first_digit  # Изменённое число
    return revers_number


def num_count(n):
    count = 0
    arr = n
    while arr > 0:
        count += 1
        arr = arr // 10
    return count


def first_number():
    first_n = int(input("Введите первое число: "))
    first_num_count = num_count(first_n)
    if first_num_count < 3:
        print("В первом числе меньше трёх цифр.")
        return 0
    else:
        first_n = (backwards_numb(first_n, first_num_count))
        print(f'Изменённое первое число = {first_n}')
        return first_n


def second_number():
    second_n = int(input("Введите второе число: "))
    second_num_count = num_count(second_n)
    if second_num_count < 4:
        print("Во втором числе меньше четырёх цифр.")
        return 0
    else:
        second_n = (backwards_numb(second_n, second_num_count))
        print(f'Изменённое второе число = {second_n}')
        return second_n


def sum_number(x, y):
    print(f'Сумма чисел: {x + y}')


sum_number(first_number(), second_number())

