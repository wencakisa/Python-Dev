import logging
from collections import defaultdict
import csv
import iso8601
import sys

logging.basicConfig(filename='errors.log', level=logging.DEBUG)


def main():
    try:
        input_filename = './sales.csv'
        sales_list = split_csv_file(input_filename)

        most_date_sales = get_most_date_sales(sales_list)
        most_hour_sales = get_most_hour_sales(sales_list)

        print(most_sales_analysis(most_date_sales, most_hour_sales))

        return 0
    except Exception as e:
        print('Error occurred: {}'.format(str(e)))
        return 1


def split_csv_file(input_filename: str) -> list:
    result = []

    with open(input_filename, encoding='utf-8') as f:
        for line_index, line in enumerate(csv.reader(f)):
            if line:
                result.append(line)
            else:
                logging.warning('Empty line: {}'.format(line_index))

    return result


def load_sales_data_by_date(sales_list: list) -> defaultdict:
    date_sales = defaultdict(list)

    for info in sales_list:
        d = iso8601.parse_date(info[0]).date()
        price = float(info[-1].strip())

        date_sales[d].append(price)

    return {date: sum(sales) for date, sales in date_sales.items()}


def load_sales_data_by_hour(sales_list: list) -> defaultdict:
    hour_sales = defaultdict(list)
    most_sales_date = get_most_date_sales(sales_list)[0]

    for info in sales_list:
        d = iso8601.parse_date(info[0])
        price = float(info[-1].strip())

        if str(d.date()) == str(most_sales_date):
            hour_sales[d.hour].append(price)

    return {hour: sum(sales) for hour, sales in hour_sales.items()}


def get_most_date_sales(sales_list: list) -> tuple:
    date_sales = load_sales_data_by_date(sales_list)
    max_date_sales_sum = max(date_sales.values())

    for date, sales_sum in date_sales.items():
        if sales_sum == max_date_sales_sum:
            return date, sales_sum


def get_most_hour_sales(sales_list: list) -> tuple:
    hour_sales = load_sales_data_by_hour(sales_list)
    max_hour_sales_sum = max(hour_sales.values())

    for hour, sales_sum in hour_sales.items():
        if sales_sum == max_hour_sales_sum:
            return hour, sales_sum


def most_sales_analysis(most_date_sales: tuple, most_hour_sales: tuple) -> str:
    most_sales_date, most_sales_date_amount = most_date_sales
    day_of_week = most_sales_date.strftime('%A')

    most_sales_hour, most_sales_hour_amount = most_hour_sales

    most_sales_date_output = 'Most sales on {} ({}): {:.2f}$'.format(
        most_sales_date, day_of_week, most_sales_date_amount
    )
    most_sales_hour_output = 'Most sales between {}-{}h: {:.2f}$'.format(
        most_sales_hour, most_sales_hour + 1, most_sales_hour_amount
    )

    return '{}\n{}'.format(most_sales_date_output, most_sales_hour_output)

if __name__ == '__main__':
    sys.exit(main())
