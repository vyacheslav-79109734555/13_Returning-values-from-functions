while True:
    amplitude = float(input('Введите начальную амплитуду: '))
    stop_amplitude = float(input('Введите амплитуду остановки: '))
    if amplitude > 0 and stop_amplitude > 0:
        print('*' * 30)
        break
    print('попробуй ввести данные еще раз: ')


def fluctuations(amplitude, stop_amplitude):
    counter = 0
    fluctuation = 8.4 / 100

    while amplitude > stop_amplitude:
        amplitude *= 1 - fluctuation
        counter += 1
    print('Маятник остановиться через', counter, 'колебаний')


fluctuations(amplitude, stop_amplitude)

