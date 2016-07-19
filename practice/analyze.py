import sys
import os
import iso8601 as iso
import csv
from datetime import timezone
from decimal import Decimal
from typing import List, Generator, Dict
from collections import Counter


def parse_cmd_line_params():
    if len(sys.argv) < 3:
        raise ValueError('Usage: {} <catalog.csv> <sales.csv>'.format(sys.argv[0]))

    filename_catalog, filename_sales = sys.argv[1:3]

    if not os.path.isfile(filename_catalog) or not os.access(filename_catalog, os.R_OK):
        raise ValueError('Invalid or inaccessible catalog file: {}'.format(filename_catalog))
    if not os.path.isfile(filename_sales) or not os.access(filename_sales, os.R_OK):
        raise ValueError('Invalid or inaccessible sales file: {}'.format(filename_sales))

    return filename_catalog, filename_sales


def load_csv_file(file: str) -> Generator:
    with open(file) as f:
        for line in csv.reader(f):
            yield line


def load_catalog_data(gen: Generator) -> List:
    return [
        {
            'item_id': el[0],
            'category': el[-3]
        }
        for el in gen
    ]


def load_sales_data(gen: Generator) -> List:
    return [
        {
            'item_id': el[0],
            'country': el[1],
            'city': el[2],
            'sale_timestamp': el[3],
            'price': el[4]
        }
        for el in gen
    ]


def test_sales_data(sales: list) -> bool:
    try:
        for sales_el in sales:
            sales_el['sale_timestamp'] = iso.parse_date(sales_el['sale_timestamp']).astimezone(timezone.utc)
            sales_el['price'] = Decimal(sales_el['price'])
        return True
    except Exception as e:
        print('Error: {}'.format(str(e)))
        return False


def get_top_sales_by_category(catalog: list, sales: list, top=1) -> Counter:
    sales_by_category = Counter()

    for catalog_item in catalog:
        for sales_item in sales:
            if catalog_item['item_id'] == sales_item['item_id']:
                sales_by_category[catalog_item['category']] += sales_item['price']

    return sales_by_category.most_common(top)


def get_top_sales_by_city(catalog: list, sales: list, top=1) -> Counter:
    cities_dict = Counter()

    for catalog_item in catalog:
        for sales_item in sales:
            key = '{} ({})'.format(sales_item['city'], sales_item['country'])
            if catalog_item['item_id'] == sales_item['item_id']:
                cities_dict[key] += sales_item['price']

    return cities_dict.most_common(top)


def get_top_sales_by_hour(sales: list, top=1) -> Counter:
    hours_dict = Counter()

    for sales_item in sales:
        date = sales_item['sale_timestamp']
        date = date.replace(minute=0, second=0).strftime('%Y-%m-%d %H:%M')
        hours_dict[date] += sales_item['price']

    return hours_dict.most_common(top)


def get_chart(prices: list, max_width=1) -> Dict:
    max_price = max(prices)
    value_per_star = max_price / max_width

    return {price: '*' * int(price / value_per_star) for price in prices}


def print_sorted(top_prices: Counter) -> None:
    max_padding = len(max([k for k, price in top_prices]))
    chart = get_chart([price for k, price in top_prices], 25)

    for k, price in top_prices:
        print('\t{:<{}} : {} {}€'.format(k, max_padding, chart[price], price))


def print_summary(sales: list) -> None:
    sales_count = len(sales)
    sales_sum = sum(sales_item['price'] for sales_item in sales)
    avg_sales_sum = sales_sum / sales_count

    dates = [el['sale_timestamp'] for el in sales]
    starting_date = min(dates)
    ending_date = max(dates)

    print(
        '''
Summary
-------
        Sales : {}
        Sales sum : {}€
        Average sales price : {}€
        Starting date : {}
        Ending date : {}
        '''.format(sales_count, sales_sum, avg_sales_sum, starting_date, ending_date)
    )


def print_top(catalog: list, sales: list, top=1) -> None:
    sales_by_category = get_top_sales_by_category(catalog, sales, top)
    sales_by_city = get_top_sales_by_city(catalog, sales, top)
    sales_by_hour = get_top_sales_by_hour(sales, top)

    print('Top {} categories prices\n-----------------------'.format(top))
    print_sorted(sales_by_category)
    print('\nTop {} cities prices\n-------------------'.format(top))
    print_sorted(sales_by_city)
    print('\nTop {} hours prices\n------------------'.format(top))
    print_sorted(sales_by_hour)


def main():
    try:
        filename_catalog, filename_sales = parse_cmd_line_params()

        catalog = load_catalog_data(load_csv_file(filename_catalog))
        sales = load_sales_data(load_csv_file(filename_sales))

        if test_sales_data(sales):
            print_summary(sales)
            print_top(catalog, sales, 7)

        return 0
    except Exception as e:
        print('Error: {}'.format(str(e)))
        return 1

if __name__ == '__main__':
    sys.exit(main())
