import sys
import csv


def main():
    product_id = input()
    sales_filename = input()

    sales_data = load_sales_data(product_id, sales_filename)
    print(get_city_with_less_price(sales_data))


def load_sales_data(product_id, sales_filename):
    with open(sales_filename, encoding='utf-8') as f:
        return [(line[2], float(line[4])) for line in csv.reader(f) if product_id == line[0]]


def get_city_with_less_price(sales_data):
    return sorted(sales_data, key=lambda n: n[1])[0][0]


if __name__ == '__main__':
    sys.exit(main())
