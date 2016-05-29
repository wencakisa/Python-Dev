import sys


def main():
    id = str(input())
    input_data = load_data(input())
    print(get_city_with_less_price(input_data, id))


def load_data(input_filename):
    with open(input_filename, encoding='utf-8') as f:
        loaded_data = []

        for line in f:
            line = line.split(',')
            loaded_data.append((line[0][1:-1], line[2][1:-1], float(line[-1])))

        return loaded_data


def get_city_with_less_price(input_data, id):
    return min([(el[1], el[2]) for el in input_data if el[0] == id], key=lambda n: n[1])[0]


if __name__ == '__main__':
    sys.exit(main())
