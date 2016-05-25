import logging
logging.basicConfig(filename='errors.log', level=logging.DEBUG)


def split_csv_file(file: str):
    splitted = []

    with open(file) as f:
        lines = f.readlines()

        for index, line in enumerate(lines):
            if line.rstrip():
                splitted.append(line.split(','))
            else:
                logging.warning('Invalid line detected on {}'.format(index))

    return splitted


def get_average_price(splitted_list: list):
    total_price = 0

    for info in splitted_list:
        total_price += float(info[-1].strip())

    avg_price = total_price / len(splitted_list)

    return round(avg_price, 2)


def get_by_gender(splitted_list: list, gender: str):
    gender_list = []

    for info in splitted_list:
        if info[len(info) - 2] == gender:
            gender_list.append(info)

    return gender_list


def grouped_by_gender(file: str):
    splitted = split_csv_file(file)
    genders = ['Infant', 'Men', 'Kid', 'Unisex', 'Woman']
    genders_dict = {}

    for gender in genders:
        genders_dict[gender] = get_average_price(
            get_by_gender(splitted, gender)
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
