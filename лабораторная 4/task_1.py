import json

def task() -> float:
    with open('input.json', 'r') as file:
        chisla = json.load(file)

    _sum = 0.0

    for item in chisla:
        _sum += item['score'] * item['weight']

    return round(_sum, 3)

print(task())
