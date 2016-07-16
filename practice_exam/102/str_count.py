import sys
from collections import Counter


def main():
    try:
        print(Counter(str(input()).strip()).most_common(1)[0][0])
    except Exception:
        print('INVALID INPUT')


if __name__ == '__main__':
    sys.exit(main())
