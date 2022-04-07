# 3) функция, которая принимает один аргумент (число = number)
def numeral_count(number):
    if number < 0:
        print('Число отрицательное ! обнуляю.')
        return 0
    count = 0
    while number > 0:
        number //= 10
        count += 1
        print(count)

    return count


# 1) запрашиваем данные пользователя:
first_Task = int(input('Введите первое число: '))
second_Task = int(input('Введите второе число: '))

# 2) создаем переменные для получения данных
first_Numeral = numeral_count(first_Task)
second_Numeral = numeral_count(second_Task)

print('первое число = : ', first_Numeral)
print('второе число = : ', second_Numeral)

if first_Numeral > second_Numeral:
    print('Цифр больше в первом числе.')
elif first_Numeral < second_Numeral:
    print('Цифр больше во втором числе.')
else:
    print('Равное колличество чисел')

print('первое число: ', first_Numeral)
print('второе число: ', second_Numeral)
