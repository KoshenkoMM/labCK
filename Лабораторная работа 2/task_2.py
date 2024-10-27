salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
i = 1
money_capital = spend
money_capital -= salary
for i in range(months - 1):
    spend *=  (1 + increase)
    money_capital += spend
    money_capital -= salary

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
