v_first_Planet = 1.43128e15  # km^3 (объем планеты)
v_second_Planet = 6.254e13  # km^3 (объем планеты)
p_Earth = 5.5153e12  # кг / km^3 (плотность планеты)

m_first_Planet = float(input('Масса первой планеты: '))  # 1.8985e27
m_second_Planet = float(input('Масса второй планеты: '))  # 1.0243e26

# вычисляем кг / km^3 // плотность планеты //
p_first_Planet = m_first_Planet / v_first_Planet
p_second_Planet = m_second_Planet / v_second_Planet

print('Плотность первой планеты', p_first_Planet)
print('Плотность второй планеты', p_second_Planet)

if abs(p_Earth - p_first_Planet) < abs(p_Earth - p_second_Planet):
    print('Плотность первой планеты ближе к плотности Земли')
else:
    print('Плотность второй планеты ближе к плотности Земли')
