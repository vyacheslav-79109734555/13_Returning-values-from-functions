print('1.1 + 2.2 = 3.3')

if (1.1 + 2.2) == 3.3:
    print('равна')

else:
    print('не равна')
    print(1.1 + 2.2)

# //////////////////////////////////

a = 1.1
b = 2.2
c = a + b
d = 3.3
# сравнивать мы можем только положительное значение а значит используем модуль // abs // от формулы (c - d)
if abs(c - d) < 1e15:
    print('равна')  # в данном случае равна
    print(c)
else:
    print('не равна')
