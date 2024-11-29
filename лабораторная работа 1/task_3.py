list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

quantity_players = len(list_players)
first = list_players[::2]
second = list_players[1::2]

print("Количество игроков:", quantity_players)
print(first,"\n", second)
