import sys


def main():
    pass


def load_data(input_filename):
    with open(input_filename) as f:
        return [line for line in f]


if __name__ == '__main__':
    sys.exit(main())
