import sys


def main():
    exchange_filename = input()
    amounts_filename = input()

    exchange_data = load_exchange_data(exchange_filename)
    amounts_data = load_amounts_data(amounts_filename)

    converted = convert_to_bgn(exchange_data, amounts_data)

    for value in converted:
        print('{:.2f}'.format(value))


def load_exchange_data(exchange_filename):
    result = []

    with open(exchange_filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip().split(' ')
            result.append((line[0], float(line[1])))

    return result


def load_amounts_data(amounts_filename):
    result = []

    with open(amounts_filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip().split(' ')
            result.append((line[1], float(line[0])))

    return result


def convert_to_bgn(exchange_data, amounts_data):
    return [
        am_price / ex_price
        for am_currency, am_price in amounts_data
        for ex_currency, ex_price in exchange_data
        if ex_currency == am_currency
    ]

if __name__ == '__main__':
    sys.exit(main())
