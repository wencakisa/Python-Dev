import sys
import csv
from typing import List


def main():
    try:
        data = load_data('./city-temperature-data.csv')
        missing_data = get_missing_data(data)
        print_missing_data(missing_data)
        return 0
    except Exception as e:
        print('INVALID INPUT. {}'.format(str(e)))


def load_data(input_filename: str) -> dict:
    with open(input_filename, encoding='utf-8') as f:
        loaded_data = {}

        for element in csv.reader(f):
            date = str(element[0])
            city = str(element[1])

            if date in loaded_data.keys():
                loaded_data[date].append(city)
            else:
                loaded_data[date] = [city]

        return loaded_data


def get_missing_data(data: dict) -> List[str]:
    return [
        '{},{}'.format(date, ','.join(set(max(data.values())).difference(set(cities))))
        for date, cities in sorted(list(data.items()), key=lambda n: n[0])
        if len(cities) != len(max(data.values()))
    ]


def print_missing_data(missing_data: list) -> None:
    [print(msg) for msg in missing_data] if missing_data else print('ALL DATA AVAILABLE')


if __name__ == '__main__':
    sys.exit(main())
