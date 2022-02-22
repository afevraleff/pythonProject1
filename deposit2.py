per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму депозита"))
deposit_percent = list(per_cent.values())
deposit_percent.sort()
print("Максимальная сумма, которую вы можете заработать", round(deposit_percent[-1]*money))