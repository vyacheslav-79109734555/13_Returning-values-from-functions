def count(numb):
    extent = 0
    if int(numb) == 0:
        while int(numb) <= 0:
            numb *= 10
            extent -= 1
        numb = round(numb, 2)
    else:
        while int(numb) > 10:
            numb /= 10
            extent += 1

    count_numb = f'x = {numb} * 10 ** {extent}\n или \n x = {round(numb, 2)}e{extent}'

    return count_numb


n = float(input('Введите число: '))
print(f'Формат плавающей точки: {count(n)}')

