# \\ Входные данные:
# Цена товара (float) - вещественное число
# Величина налога (int) - целое число
# \\ Выходные данные:
# Итоговая цена:

# 4) внутри функции def
def calculate_Tax(price, tax):
    # 5) мы производим различные действия : решение примера используя аргументы:
    total = price + (price * tax / 100)
    print(total)
    # команда return (с анг. ВЕРНУТЬ) возвращает значение и перекидывает его в
    # переменную:___________________total_Price = calculate_Tax(my_Price, my_Tax)
    # 6) записываем результат в переменную : total_Price стр. 24
    return total


# 1) запрашиваем у пользователя нужные значения:
my_Price = float(input('Введите цену товара: '))
my_Tax = int(input('Введите величину налога: '))

# 2) назначаем переменную в которую нужно вернуть посчитанное значение из формулы функции def: total_Price
# 3) присваиваем ее вызов функции с нужными нам пораметрами: calculate_Tax(my_Price, my_Tax)
total_Price = calculate_Tax(my_Price, my_Tax)

new_Tax = int(input('Введите новый налог: '))
total_Price = calculate_Tax(total_Price, my_Tax)

print(total_Price)
