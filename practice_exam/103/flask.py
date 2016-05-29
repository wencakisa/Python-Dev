import sys


def main():
    try:
        wall_w = float(input())
        wall_h = float(input())
        print(count_flasks_to_paint(wall_w, wall_h))
        return 0
    except Exception as e:
        print('Error: {}'.format(str(e)))


def count_flasks_to_paint(wall_w, wall_h):
    flask_area = 1.76
    wall_area = wall_w * wall_h
    count = 1

    while flask_area < wall_area:
        flask_area += 1.76
        count += 1

    return count


if __name__ == '__main__':
    sys.exit(main())
