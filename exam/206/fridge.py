import sys
import csv


def main():
    input_data = load_data(input())
    opening_dates = get_opening_dates(input_data)
    for opening_date in opening_dates:
        print(opening_date)


def load_data(input_filename):
    with open(input_filename) as f:
        return [(line[0], float(line[1])) for line in csv.reader(f)]


def get_opening_dates(input_data):
    dates = set()
    for i, j in enumerate(input_data[:-1]):
        if input_data[i][1] - input_data[i + 1][1] >= 4:
            dates.add(input_data[i][0])
        elif input_data[i + 1][1] - input_data[i][1] >= 4:
            dates.add(input_data[i + 1][0])

    return sorted(dates)


if __name__ == '__main__':
    sys.exit(main())
