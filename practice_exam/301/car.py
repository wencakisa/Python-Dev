import sys


def main():
    try:
        input_filename = input()  # '301-1-distances.txt'
        input_data = load_data(input_filename)
        print(round(sum(input_data), 2))
    except Exception:
        print('INVALID INPUT')


def load_data(input_filename):
    result = []

    with open(input_filename, encoding='utf-8') as f:
        for line in f:
            line = line.split(',')
            result.append((int(line[1]) - int(line[0]) + 1) / int(line[2]))

    return result

if __name__ == '__main__':
    sys.exit(main())
