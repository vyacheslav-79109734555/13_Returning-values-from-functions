# 8) в функцию // def numeral_count(num): // получила число ( number ) со строки 45
#    в итоге // num = number // со стр 45
def numeral_count(num):
    n = 0
    # 9) пока // while num > 0: // получаем количество знаков в // num = number //
    while num > 0:
        n += 1
        num //= 10
    # 10) возвращаем данные // n // полученных после вычисления в стр 46
    return n


# 1) запрашиваем данные пользователя: // num // - всего задач
num_ = int(input('Введите кол-во задач: '))
# 2) переменная // max_Num // счетчик чисел
max_Num = 0
# 3) переменная // final_Num // максимального числа
final_Num = 0
# 4) переменная // а // максимального количество цифр в числе
a = 0
# 5) через цикл // for i in range(num) // получаем искомые данные пользователя: Ввод чисел ...
for i in range(num_):
    # 6) каждая итерация отправляет в функцию // def numeral_count(num): // для пересчета цифр стр 24
    number = int(input('Введите число: '))
    # 7) вызов функции // def numeral_count(num): // стр 24
    # // (number) // передает число в функцию на стр 24 // def numeral_count(num): //
    # // x // получает число из функцию на стр 28 // def numeral_count(num): // -- количество цифр в числе
    x = numeral_count(number)

    # 11) // if x > a // получает число из функцию на стр 46 //
    if x > a:
        a = x
    # просто проверка // х //
    print('x =', x)
    # print(number)
    # 12) // if number <= 0: // ищем наибольшее кол-во цифр в числе
    if number <= 0:
        number = 0
    elif max_Num <= x:
        final_Num = number
        max_Num = x

print('Первая задача на обработку:', final_Num)
print('максимального количество цифр в числе = ', a)
