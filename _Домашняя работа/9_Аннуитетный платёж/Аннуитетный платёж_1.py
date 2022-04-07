def monthly_Payment(credit, period, percent):  # ежемесячный платеж
    percent = percent / 100
    k = (percent * (1 + percent) ** period) / ((1 + percent) ** period - 1)
    payment = round(k * credit, 2)  # платеж
    # print('+', payment)
    return payment  # платеж


def payments(credit, percent, payment, convention):
    for i in range(1, convention + 1):  # // i // Период
        pay_percent = credit * percent / 100  # // pay_percent // Выплачено процентов
        pay_credit = payment - pay_percent  # // pay_credit // Выплачено тела кредита
        print('\nПериод', i)
        print('\nОстаток долга на начало периода:', credit)
        print('Выплачено процентов:', pay_percent)
        print('Выплачено тела кредита:', pay_credit)
        credit -= pay_credit
        print('**************', credit)

    return credit


credit = float(input('Введите сумму кредита: '))
period = int(input('На сколько лет выдан кредит? '))
percent = float(input('Сколько процентов годовых? '))
# convention = int(input('Договор? '))
count_percent = 0

payment = monthly_Payment(credit, period, percent)
new_credit = payments(credit, percent, payment, 4)
new_period = int(input('\nНа сколько лет продляется договор № 2? '))
new_percent = float(input('Увеличение ставки по договору № 2 до: '))
new_period = new_period + period - 4
payment = monthly_Payment(new_credit, new_period, new_percent)
new_credit = payments(new_credit, new_percent, payment, new_period)

print('\nОстаток долга:', new_credit)
print('\nnew_period:', new_period)

