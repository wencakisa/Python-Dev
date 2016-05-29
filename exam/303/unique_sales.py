import sys
import csv
from collections import defaultdict


def main():
    try:
        sales_filename = 'sales.csv'  # input()
        sales_data = load_sales_data(sales_filename)
        unique_sales_by_city = get_unique_sales_by_city(sales_data)

        if len(unique_sales_by_city) > 0:
            for city, identifiers in sorted(unique_sales_by_city.items(), key=lambda n: n[0]):
                print(','.join([city] + identifiers))
        else:
            print('NO UNIQUE SALES')
    except Exception:
        print('INVALID INPUT')


def load_sales_data(sales_filename):
    result = defaultdict(list)

    with open(sales_filename, encoding='utf-8') as f:
        for row in csv.reader(f):
            result[row[0]].append((row[2], float(row[-1])))

    return result


def get_unique_sales_by_city(sales_data):
    unique = defaultdict(list)

    for identifier, cities in sales_data.items():
        if len(cities) == 1:
            unique[cities[0][0]].append(identifier)

    return unique


if __name__ == '__main__':
    sys.exit(main())
