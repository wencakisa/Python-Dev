import sys
import math

LOSS_PERCENT = 0.098
LOSS_MULTIPLIER = 1 + LOSS_PERCENT


def main():
    try:
        sheet_area = 0.80
        box_w = 1.23
        box_h = 0.78
        box_d = 0.50

        box_surface_area = 2 * (
            box_w * box_h +
            box_w * box_d +
            box_h * box_d
        )

        box_surface_area *= LOSS_MULTIPLIER

        print(math.ceil(box_surface_area / sheet_area))
        return 0
    except Exception as e:
        print('INVALID INPUT: {}'.format(e))


if __name__ == '__main__':
    sys.exit(main())
