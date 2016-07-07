import sys
import csv


def main():
    try:
        box_w = float(input())
        box_h = float(input())
        box_d = float(input())
        input_filename = str(input())

        input_data = load_data(input_filename)
        box_dimensions = sorted((box_w, box_h, box_d))

        result = get_suitable(input_data, box_dimensions)

        print('\n'.join(result))

        return 0
    except Exception:
        print('INVALID INPUT')


def load_data(input_filename):
    with open(input_filename, encoding='utf-8') as f:
        return [(line[0], sorted([float(line[1]), float(line[2]), float(line[3])])) for line in csv.reader(f)]


def get_suitable(input_data, box_dimensions):
    return [
        name
        for name, dimensions in input_data
        if all(dimensions[dim_index] <= box_dimensions[dim_index] for dim_index in range(3))
    ]


if __name__ == '__main__':
    sys.exit(main())
