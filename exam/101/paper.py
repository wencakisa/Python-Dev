import sys
import math

LOSS_PERCENT = 0.098
LOSS_MULTIPLIER = 1 + LOSS_PERCENT


def main():
    try:
        sheet_area = float(input())
        box_w = float(input())
        box_h = float(input())
        box_d = float(input())

        box_surface_area = 2 * (
            box_w * box_h +
            box_w * box_d +
            box_h * box_d
        )

        box_surface_area *= LOSS_MULTIPLIER

        print(math.ceil(box_surface_area / sheet_area))

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


if __name__ == '__main__':
    sys.exit(main())
