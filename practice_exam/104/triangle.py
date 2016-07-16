import sys
from math import sqrt


def main():
    try:
        a = float(input())
        b = float(input())
        c = float(input())

        print('{:.2f}'.format(get_area(a, b, c)))

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def get_area(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))


if __name__ == '__main__':
    sys.exit(main())
