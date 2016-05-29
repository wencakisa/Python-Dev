import sys
import csv


def main():
    try:
        box_w = float(input())
        box_h = float(input())
        box_d = float(input())
        input_filename = str(input())

        box_dimensions = sorted((box_w, box_h, box_d))
        input_data = load_data(input_filename)

        fittable = get_fittable(input_data, box_dimensions)

        for name in fittable:
            print(name)

        return 0
    except Exception as e:
        print('INVALID INPUT: {}'.format(str(e)))


def load_data(input_filename):
    with open(input_filename, encoding='utf-8') as f:
        return [(row[0], sorted([float(row[1]), float(row[2]), float(row[3])])) for row in csv.reader(f)]


def get_fittable(input_data, box_dimensions):
    return [
        name for name, dimensions in input_data
        if all(dimensions[dim_index] <= box_dimensions[dim_index] for dim_index in range(3))
    ]


if __name__ == '__main__':
    sys.exit(main())
