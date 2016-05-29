import sys


def main():
    try:
        input_data = load_data(input())
        print('{:.2f}'.format(get_time_to_arrive(input_data)))
    except Exception as e:
        print('INVALID INPUT: {}'.format(str(e)))


def load_data(input_filename):
    with open(input_filename, encoding='utf-8') as f:
        loaded_data = []

        for line in f:
            line = line.split(',')
            loaded_data.append((int(line[1]) - int(line[0]) + 1, int(line[2])))

        return loaded_data


def get_time_to_arrive(input_data):
    time_to_arrive = 0

    for pair in input_data:
        time_to_arrive += pair[0] / pair[1]

    return time_to_arrive


if __name__ == '__main__':
    sys.exit(main())
