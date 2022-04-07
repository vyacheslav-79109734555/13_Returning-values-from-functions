max_value = 4  # минимальный уровень опасности
min_value = 0  # максимальный уровень опасности

max_danger = float(input('Введите допустимый уровень опасности: '))

depth = min_value + (max_value - min_value) / 2  # глубина
danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10  # опасность
if max_danger < 0:
    print('Ошибка: Уровень опасности - абсолютная величина и должна быть больше "0"')
else:
    print(f'Глубина: {round(depth, 4)} Опасность {round(danger, 4)}')
    while abs(danger) > max_danger:
        if danger > 0:
            min_value = depth
        else:
            max_value = depth
        depth = min_value + (max_value - min_value) / 2  # глубина
        danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
    print(f'Глубина:{round(depth, 4)} Опасность {round(danger, 4)}')
print(f'Приблизительная глубина безопасной кладки: {round(depth, 4)}')

