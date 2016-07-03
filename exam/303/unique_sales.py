import sys
import csv
from collections import defaultdict


def main():
    try:
        input_filename = 'sales.csv'  # input()
        input_data = load_sales_data(input_filename)
        unique_sales_data = get_unique_sales(input_data)

        if not unique_sales_data:
            raise Exception('NO UNIQUE SALES')

        for city, items in sorted(unique_sales_data.items(), key=lambda n: n[0]):
            print(','.join([city] + items))

    except Exception:
        print('INVALID INPUT')


def load_sales_data(input_filename):
    with open(input_filename, encoding='utf-8') as f:
        return [(line[0], line[2]) for line in csv.reader(f)]


def get_unique_sales(input_data):
    sales_dict = defaultdict(list)
    unique_sales = defaultdict(list)

    for pair in input_data:
        sales_dict[pair[0]].append(pair[1])

    for item_id, cities in sales_dict.items():
        if len(cities) == 1:
            unique_sales[cities[0]].append(item_id)

    return unique_sales


if __name__ == '__main__':
    sys.exit(main())
