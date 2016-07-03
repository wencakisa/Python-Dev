import sys
import csv
from collections import defaultdict


def main():
    try:
        input_filename = 'city-temperature-data.csv'  # input()
        input_data = load_data(input_filename)
        missing_data = get_missing_data(input_data)

        if not missing_data:
            raise Exception('ALL DATA AVAILABLE')

        for date, cities in sorted(missing_data, key=lambda n: n[0]):
            print(','.join([date] + cities))

    except Exception as e:
        print('INVALID INPUT: {}'.format(e))


def load_data(input_filename):
    with open(input_filename, encoding='utf-8') as f:
        return [(line[0], line[1]) for line in csv.reader(f)]


def get_missing_data(input_data):
    input_data_dict = defaultdict(list)

    for pair in input_data:
        input_data_dict[pair[0]].append(pair[1])

    all_cities = set(max(input_data_dict.values()))

    return [
        (date, list(all_cities.difference(set(cities))))
        for date, cities in input_data_dict.items()
        if len(cities) != len(all_cities)
    ]


if __name__ == '__main__':
    sys.exit(main())
