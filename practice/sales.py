from decimal import Decimal, InvalidOperation
from datetime import timezone

import iso8601

EXPECTED_COLUMNS = 5

KEY_ITEM_ID = 'item_id'
KEY_ITEM_PRICE = 'price'
KEY_ITEM_COUNTRY = 'country'
KEY_ITEM_CITY = 'city'
KEY_ITEM_TS = 'ts'

COLUMN_ITEM_ID = 0
COLUMN_ITEM_COUNTRY = 1
COLUMN_ITEM_CITY = 2
COLUMN_ITEM_TS = 3
COLUMN_ITEM_PRICE = 4


def load_sales_data(gen) -> list:
    return [
        {
            KEY_ITEM_ID: row[COLUMN_ITEM_ID],
            KEY_ITEM_COUNTRY: row[COLUMN_ITEM_COUNTRY],
            KEY_ITEM_CITY: row[COLUMN_ITEM_CITY],
            KEY_ITEM_TS: row[COLUMN_ITEM_TS],
            KEY_ITEM_PRICE: row[COLUMN_ITEM_PRICE]
        }
        for row in gen
        if len(row) == EXPECTED_COLUMNS
    ]


def test_sales_data(sales) -> bool:
    for sale in sales:
        try:
            sale[KEY_ITEM_TS] = iso8601.parse_date(sale[KEY_ITEM_TS]).astimezone(timezone.utc)
            sale[KEY_ITEM_PRICE] = Decimal(sale[KEY_ITEM_PRICE])
        except iso8601.ParseError as pe:
            print(str(pe))
            return False
        except InvalidOperation:
            print('Unable to parse decimal {}'.format(sale[KEY_ITEM_PRICE]))
            return False

    return True
