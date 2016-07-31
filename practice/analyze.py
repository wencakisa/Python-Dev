import sys
import os
import csv

from practice.catalog import load_catalog_data
from practice.sales import load_sales_data, test_sales_data
from practice.analyze_functions import get_summary, get_sales_by_category, get_sales_by_city, get_sales_by_ts
from practice.print_functions import print_summary, print_sales_by_criteria


def main():
    try:
        catalog_filename, sales_filename = parse_cmd_line_params()

        print('. . . Извличане на информация за продажби . . .')

        catalog = load_catalog_data(load_csv_file(filename=catalog_filename))
        sales = load_sales_data(load_csv_file(filename=sales_filename))

        if test_sales_data(sales):
            sales_grouped_by_criteria = [
                ('Сума на продажби по категории', get_sales_by_category(catalog, sales)),
                ('Сума на продажби по градове', get_sales_by_city(sales)),
                ('Часове с най-голяма сума продажби', get_sales_by_ts(sales))
            ]

            print_summary(get_summary(sales))

            for criteria_title, sales_by_criteria in sales_grouped_by_criteria:
                print_sales_by_criteria(title=criteria_title, sales=sales_by_criteria)
                print('')

        return 0
    except Exception as e:
        print('Error: {}'.format(str(e)))
        return 1


def parse_cmd_line_params() -> tuple:
    if len(sys.argv) < 3:
        raise ValueError('Usage: analyze.py <catalog.csv> <sales.csv>')

    catalog_filename, sales_filename = sys.argv[1:3]

    if not os.path.isfile(catalog_filename) or not os.access(catalog_filename, os.R_OK):
        raise ValueError('Invalid or inaccessible catalog file: {}'.format(catalog_filename))
    if not os.path.isfile(catalog_filename) or not os.access(catalog_filename, os.R_OK):
        raise ValueError('Invalid or inaccessible sales file: {}'.format(sales_filename))

    return catalog_filename, sales_filename


def load_csv_file(filename: str):
    with open(filename, mode='r', encoding='utf-8') as f:
        yield from csv.reader(f)

if __name__ == '__main__':
    sys.exit(main())
