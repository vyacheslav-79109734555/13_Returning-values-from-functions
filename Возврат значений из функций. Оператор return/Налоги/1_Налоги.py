def calculate_Tax(price, tax):
    # решение примера используя аргументы:
    total = price + (price * tax / 100)
    print('Итоговая цена с налогом', total)


# запрашиваем у пользователя нужные значения:
my_Price = float(input('Введите цену товара: '))
my_Tax = int(input('Введите величину налога: '))

# вызываем функию в которую передаем значения (my_Price, my_Tax) в виде аргументов:
calculate_Tax(my_Price, my_Tax)
