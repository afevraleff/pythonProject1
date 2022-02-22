per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму депозита"))
t_list = list(per_cent.values())
deposit = [t_list[0]*money, t_list[1]*money, t_list[2]*money, t_list[3]*money]
deposit = list(map(round, deposit))

print("Максимальная сумма, которую вы можете заработать", max(deposit))