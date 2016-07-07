import logging
logging.basicConfig(filename='errors.log', level=logging.DEBUG)


def split_csv_file(file: str):
    result = []

    with open(file) as f:
        lines = f.readlines()

        for index, line in enumerate(lines):
            if line.rstrip():
                result.append(line.split(','))
            else:
                logging.warning('Invalid line detected on {}'.format(index))

    return result


def get_average_price(input_data: list):
    total_price = 0

    for info in input_data:
        total_price += float(info[-1].strip())

    avg_price = total_price / len(input_data)

    return round(avg_price, 2)


def get_by_gender(input_data: list, gender: str):
    gender_list = []

    for info in input_data:
        if info[len(info) - 2] == gender:
            gender_list.append(info)

    return gender_list


def grouped_by_gender(file: str):
    result = split_csv_file(file)
    genders = ['Infant', 'Men', 'Kid', 'Unisex', 'Woman']
    genders_dict = {}

    for gender in genders:
        genders_dict[gender] = get_average_price(
            get_by_gender(result, gender)
        )

    return genders_dict


def print_grouped_dict(dictionary: dict):
    for k, v in dictionary.items():
        print("{}\n\t-> {}".format(k, v))


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

if __name__ == '__main__':
    main()
