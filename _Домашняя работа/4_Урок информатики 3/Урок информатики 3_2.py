def program(numb):
    exponent = 0
    mantissa = ''
    for sumb in str(numb):
        if sumb == 'e':
            break
        elif sumb == '.':
            break
        mantissa += sumb
    if int(numb) > 10:
        while numb > 10:
            numb /= 10
            exponent += 1
    while numb < 10:
        numb *= 10
        exponent += 1
    print(f'Мантисса числа: {mantissa} \nПорядок: {exponent-1}')


numb = float(input('Введите экспоненциальную форму числа:  '))

program(numb)

