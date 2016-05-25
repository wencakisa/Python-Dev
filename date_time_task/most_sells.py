from datetime import datetime
import logging

logging.basicConfig(filename='errors.log', level=logging.DEBUG)


def split_csv_file(file):
    splitted = []

    with open(file) as f:
        lines = f.readlines()

        for ind, line in enumerate(lines):
            if line.rstrip():
                splitted.append(line.split(','))
            else:
                logging.warning('Invalid line detected on {}'.format(ind + 1))

    return splitted


def get_most_date_sales(sales):
    date_sales = {}

    for info in sales:
        date_time = datetime.strptime(info[0], '%Y-%m-%d %H:%M:%S')
        formatted_date = date_time.date().strftime('%Y-%m-%d')
        price = float(info[-1].strip())

        if formatted_date in date_sales:
            date_sales[formatted_date].append(price)
        else:
            date_sales[formatted_date] = [price]

    date_sales_sum = {date: sum(sales) for date, sales in date_sales.items()}
    max_date_sales_sum = max(date_sales_sum.values())

    for date, sales_sum in date_sales_sum.items():
        if sales_sum == max_date_sales_sum:
            return date, round(sales_sum, 2)


def get_most_hour_sales(sales):
    hour_sales = {}
    most_sales_date = get_most_date_sales(sales)[0]

    for info in sales:
        date_time = datetime.strptime(info[0], '%Y-%m-%d %H:%M:%S')
        formatted_date = date_time.date().strftime('%Y-%m-%d')
        price = float(info[-1].strip())

        if formatted_date == most_sales_date:
            if date_time.hour in hour_sales:
                hour_sales[date_time.hour].append(price)
            else:
                hour_sales[date_time.hour] = [price]

    hour_sales_sum = {hour: sum(sales) for hour, sales in hour_sales.items()}
    max_hour_sales_sum = max(hour_sales_sum.values())

    for hour, sales_sum in hour_sales_sum.items():
        if sales_sum == max_hour_sales_sum:
            return hour, round(sales_sum, 2)


def get_most_sales(sales):
    most_sales_date = get_most_date_sales(sales)[0]
    most_sales_date_amount = get_most_date_sales(sales)[1]
    most_sales_hour = get_most_hour_sales(sales)[0]
    most_sales_hour_amount = get_most_hour_sales(sales)[1]

    date_time = datetime.strptime(most_sales_date, '%Y-%m-%d')
    day_of_week = date_time.date().strftime('%A')

    most_sales_date_output = 'Most sales on {} ({}): {}$'.format(
        most_sales_date, day_of_week, most_sales_date_amount
    )
    most_sales_hour_output = 'Most sales between {}-{}h: {}$'.format(
        most_sales_hour, most_sales_hour + 1, most_sales_hour_amount
    )

    return '{}\n{}'.format(most_sales_date_output, most_sales_hour_output)


def main():
    file = './sales.csv'
    sales = split_csv_file(file)
    print(get_most_sales(sales))

if __name__ == '__main__':
    main()
