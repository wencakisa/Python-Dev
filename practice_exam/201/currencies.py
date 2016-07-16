import sys


def main():
    try:
        exchange_filename = input()  # 'exchange.txt'
        amounts_filename = input()  # 'amounts.txt'

        exchange_data = load_exchange_data(exchange_filename)
        amounts_data = load_amounts_data(amounts_filename)

        converted_data = convert_to_bgn(exchange_data, amounts_data)

        for price in converted_data:
            print('{:.2f}'.format(price))

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_exchange_data(exchange_filename):
    result = []

    with open(exchange_filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip().split(' ')
            result.append((float(line[1]), line[0]))

    return result


def load_amounts_data(amounts_filename):
    result = []

    with open(amounts_filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip().split(' ')
            result.append((float(line[0]), line[1]))

    return result


def convert_to_bgn(exchange_data, amounts_data):
    return [
        am_price / ex_price
        for am_price, am_currency in amounts_data
        for ex_price, ex_currency in exchange_data
        if ex_currency == am_currency
    ]


if __name__ == '__main__':
    sys.exit(main())
