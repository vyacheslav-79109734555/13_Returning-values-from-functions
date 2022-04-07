import math

precision = float(input('Введите точность: '))
result = 0
i = 0
added_variable = 1
while added_variable > precision:
    added_variable = 1 / math.factorial(i)
    result += added_variable
    i += 1
print('Результат:', result)
print('Константа из библиотеки math:', math.e)

