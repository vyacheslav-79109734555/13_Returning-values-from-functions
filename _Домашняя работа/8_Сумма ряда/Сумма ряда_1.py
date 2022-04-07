def factorial_n(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial


def degree_n(x, n):
    count = 1
    for i in range(1, n + 1):
        count = count * x
    return count


precision = float(input('Введите точность вычисления: '))
numb_x = float(input('Введите действительное число "х" '))
temp = 1
result = 0
n = 0

while abs(temp) > precision:
    temp = degree_n(-1, n) * (degree_n(numb_x, (2 * n)) / factorial_n(2 * n))
    result += temp
    n += 1
print("Сумма ряда =", result)

