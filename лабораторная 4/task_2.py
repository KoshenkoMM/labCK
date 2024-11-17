import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Открываем CSV файл для чтения
    with open(INPUT_FILENAME, 'r', newline='') as csv_file:
        # Создаем объект CSV читателя для разбора файла
        reader = csv.DictReader(csv_file)

        # Преобразуем данные в список словарей
        data = [row for row in reader]  # Получаем список записей

    # Открываем JSON файл для записи
    with open(OUTPUT_FILENAME, 'w') as json_file:
        # Сериализуем данные в JSON с отступами равными 4
        json.dump(data, json_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
