def mars(max_dan):
    max_value = 4
    min_value = 0
    depth = min_value - (max_value - min_value) / 2
    danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
    while abs(danger) >= max_dan:
        if danger > 0:
            min_value = depth
        else:
            max_value = depth
        depth = min_value + (max_value - min_value) / 2
        danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
    print(f'Приблизительная глубина безопасной кладки: {round(depth, 4)} м')


while True:
    try:
        max_danger = float(input('Введите уровень опасности: '))
        if max_danger > 0:
            mars(max_danger)
            break
        else:
            print('Уровень опасности не может быть отрицательным!')
    except ValueError:
        print('Введите корректные данные!')

