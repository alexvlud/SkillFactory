per_cent = {'ТКБ' : 5.6, 'СКБ' : 5.9, 'ВТБ' : 4.28, 'СБЕР' : 4.0}
money = float(input("Введите сумму вклада: "))
percent_list = list(per_cent.values())
deposit = list(map(lambda x: x*money/100, percent_list))
print("Размер вклада - ", money)
print("Deposits -", deposit)
print("Максимальная сумма, которую вы можете заработать - ", max(deposit))