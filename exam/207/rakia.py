import sys
from math import pi


def main():
    try:
        litres = float(input())
        input_filename = str(input())

        containers = load_data(input_filename)
        print(get_smallest_suitable_container(litres, containers))

        return 0
    except Exception as e:
        print('INVALID INPUT. {}'.format(str(e)))


def load_data(input_filename):
    with open(input_filename, encoding='utf-8') as f:
        loaded = []

        for line in f:
            data = line.strip().split(',')

            if len(data) != 3:
                raise ValueError('Wrong parameters count: {}'.format(line))

            if data:
                loaded.append({
                    'name': str(data[0]),
                    'radius': float(data[1]),
                    'height': float(data[2])
                })

        return loaded


def get_smallest_suitable_container(litres, containers):
    suitable_containers = []

    for container in containers:
        capacity = (pi * container['radius'] ** 2 * container['height']) / 1000

        if capacity >= litres:
            suitable_containers.append((container['name'], capacity))

    if suitable_containers:
        return min(sorted(suitable_containers, key=lambda pair: pair[1]))[0]
    else:
        raise ValueError('NO SUITABLE CONTAINERS.')


if __name__ == '__main__':
    sys.exit(main())
