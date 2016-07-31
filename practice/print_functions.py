from collections import Counter


def get_title_lines(title: str) -> str:
    return '-' * len(title)


def print_summary(summary: tuple) -> None:
    total_sales_count, total_sales_amount, avg_sales_amount, sales_start_ts, sales_end_ts = summary

    title = 'Обобщение'

    print('''{title}
{lines}
Общ брой продажби : {total_count}
Обща сума продажби : {total_amount:.2f} €
Средна цена на продажби : {average_amount:.2f} €
Начало на период на данните : {start_ts}
Край на период на данните : {end_ts}
'''.format(title=title,
           lines=get_title_lines(title),
           total_count=total_sales_count,
           total_amount=total_sales_amount,
           average_amount=avg_sales_amount,
           start_ts=sales_start_ts,
           end_ts=sales_end_ts
           ))


def print_sales_by_criteria(title: str, sales: Counter, top: int = 5) -> None:
    top_sales = sales.most_common(top)

    max_padding = max(len(category) for category, _ in top_sales)

    print('{} (top {})\n{}'.format(title, top, get_title_lines(title)))
    for category, price in top_sales:
        print('\t{:<{}} : {:.2f} €'.format(category, max_padding, price))
