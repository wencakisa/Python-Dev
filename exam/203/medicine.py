import sys


def main():
    try:
        box_w = float(input())
        box_h = float(input())
        box_d = float(input())
        input_filename = str(input())
        input_data = load_data(input_filename)
        fittable = get_fittable(input_data, box_w, box_h, box_d)

        for name in fittable:
            print(name)

    except Exception as e:
        print('INVALID INPUT: {}'.format(str(e)))


def load_data(input_filename):
    with open(input_filename) as f:
        return [line.strip().split(',') for line in f]


def get_fittable(input_data, box_w, box_h, box_d):
    # TODO: Finish this shit.

    fittable = []

    return fittable


if __name__ == '__main__':
    sys.exit(main())
