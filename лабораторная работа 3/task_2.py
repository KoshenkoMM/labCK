# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, raz=','):
    participants1 = group1.split(raz)
    participants2 = group2.split(raz)
    common_participants = set(participants1) & set(participants2)
    sorted_common_participants = sorted(common_participants)

    return sorted_common_participants

# Примеры входных данных
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, raz='|')

print(f"Общие участники: {common_participants}")