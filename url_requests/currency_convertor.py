import sys
import requests
from decimal import Decimal

API_URL = 'http://api.fixer.io/{}?base={}'
API_TIMEOUT = 20


def main():
    base_currency = str(input('From: '))
    base_amount = Decimal(input('Enter amount: '))
    target_currency = str(input('To: '))
    date = str(input('From date (yyyy-mm-dd): '))

    print('. . . Getting exchange rates . . .')
    resp = requests.get(API_URL.format(date, base_currency), timeout=API_TIMEOUT)

    if resp.status_code != 200:
        print('Unknown currency: {}'.format(base_currency))
        return 1

    exchange_rates = resp.json().get('rates', {})
    exchange_rate_to_target_currency = exchange_rates.get(target_currency, None)

    if exchange_rate_to_target_currency:
        exchange_rate_to_target_currency = Decimal(exchange_rate_to_target_currency)
    else:
        print('Unknown currency: {}'.format(target_currency))
        return 1

    target_amount = base_amount * Decimal(exchange_rate_to_target_currency)

    print('{:.2f} {} = {:.2f} {}'.format(base_amount, base_currency, target_amount, target_currency))


if __name__ == '__main__':
    sys.exit(main())
