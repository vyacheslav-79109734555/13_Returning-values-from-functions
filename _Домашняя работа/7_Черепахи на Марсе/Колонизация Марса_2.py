
def mars():
    max_value = 4
    min_value = 0
    while max_value - min_value >= max_danger:
        temp = (min_value + max_value) / 2
        counter = (min_value ** 3 - 3 * min_value ** 2 - 12 * min_value + 10) * \
                  (temp ** 3 - 3 * temp ** 2 - 12 * temp + 10)
        if counter < 0:
            max_value = temp
            print(f'Глубина: {round(min_value, 4)} Опасность {round(counter, 4)}')
        else:
            min_value = temp
    print(f'Приблизительная глубина безопасной кладки: {(max_value + min_value) / 2} м')


max_danger = float(input('Введите уровень опасности: '))

mars()

