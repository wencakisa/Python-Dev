import logging
import csv

logging.basicConfig(filename='errors.log', level=logging.DEBUG)


def main():
    file = './file_tasks/catalog_sample.csv'
    grouped = grouped_by_gender(file)
    print_grouped_dict(grouped)
    # Needs to be 785.54
    print("Total: {}".format(get_average_price(split_csv_file(file))))

    print('*' * 50)

    file = './file_tasks/catalog_full.csv'
    grouped = grouped_by_gender(file)
    print_grouped_dict(grouped)
    # Needs to be 805.82
    print("Total: {}".format(get_average_price(split_csv_file(file))))


def split_csv_file(input_filename: str) -> list:
    result = []

    with open(input_filename, encoding='utf-8') as f:
        for line_index, line in enumerate(csv.reader(f)):
            if line:
                result.append(line)
            else:
                logging.warning('Empty line: {}'.format(line_index))

    return result


def get_average_price(input_data: list) -> float:
    total_price = 0

    for info in input_data:
        total_price += float(info[-1].strip())

    avg_price = total_price / len(input_data)

    return round(avg_price, 2)


def get_by_gender(input_data: list, gender: str) -> list:
    return [info for info in input_data if info[-2] == gender]


def grouped_by_gender(input_filename: str) -> dict:
    result = split_csv_file(input_filename)
    genders = ['Infant', 'Men', 'Kid', 'Unisex', 'Woman']
    genders_dict = {}

    for gender in genders:
        genders_dict[gender] = get_average_price(
            get_by_gender(result, gender)
        )

    return genders_dict


def print_grouped_dict(dictionary: dict) -> None:
    for k, v in dictionary.items():
        print("{}: {}".format(k, v))

if __name__ == '__main__':
    main()
