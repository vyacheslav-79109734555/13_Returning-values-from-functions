def fluctuations(amp, stop):
    count = 0
    while amp > stop:
        amp -= amp * 8.4 / 100
        count += 1
    return count

    pass


while True:
    try:
        amplitude = float(input('Введите начальную амплитуду: '))
        stop_amplitude = float(input('Введите амплитуду остановки: '))
        if amplitude > stop_amplitude:
            print(f'Маятник считается остановившимся через: {fluctuations(amplitude, stop_amplitude)} колебаний')
            break
        else:
            print('Ошибка ввода! амплитуду остановки выше начальной амплитуды')
    except ValueError:
        print('Введите данные')

