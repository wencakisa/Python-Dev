from collections import Counter
from typing import List

from practice.sales import KEY_ITEM_ID, KEY_ITEM_PRICE, KEY_ITEM_CITY, KEY_ITEM_COUNTRY, KEY_ITEM_TS


def get_summary(sales: List[dict]) -> tuple:
    total_sales_count = len(sales)
    total_sales_amount = sum(sale[KEY_ITEM_PRICE] for sale in sales)
    avg_sales_amount = total_sales_amount / total_sales_count if total_sales_count else None
    sale_timestamps = [sale[KEY_ITEM_TS] for sale in sales]

    return total_sales_count, total_sales_amount, avg_sales_amount, min(sale_timestamps), max(sale_timestamps)


def get_sales_by_category(catalog: dict, sales: List[dict]) -> Counter:
    sales_by_category = Counter()

    for sale in sales:
        item_id = sale[KEY_ITEM_ID]
        price = sale[KEY_ITEM_PRICE]
        category = catalog.get(item_id, None)

        sales_by_category[category] += price

    return sales_by_category


def get_sales_by_city(sales: List[dict]) -> Counter:
    sales_by_city = Counter()

    for sale in sales:
        price = sale[KEY_ITEM_PRICE]
        city = '{} ({})'.format(sale[KEY_ITEM_CITY], sale[KEY_ITEM_COUNTRY])

        sales_by_city[city] += price

    return sales_by_city


def get_sales_by_ts(sales: List[dict]) -> Counter:
    sales_by_ts = Counter()

    for sale in sales:
        price = sale[KEY_ITEM_PRICE]
        ts = sale[KEY_ITEM_TS].replace(minute=0, second=0).strftime('%Y-%m-%d %H:%M')

        sales_by_ts[ts] += price

    return sales_by_ts
