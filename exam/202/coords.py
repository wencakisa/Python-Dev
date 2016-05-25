import sys

STEP_DIRECTION_X_MAPPING = {
    'right': 1,
    'left': -1,
}

STEP_DIRECTION_Y_MAPPING = {
    'up': 1,
    'down': -1,
}


def main():
    try:
        input_filename = './steps.txt'
        with open(input_filename, encoding='utf-8') as f:
            steps_x_y = list(load_steps_as_x_y(f))
            if steps_x_y:
                print('X {:.3f}'.format(sum(i[0] for i in steps_x_y)))
                print('Y {:.3f}'.format(sum(i[1] for i in steps_x_y)))
            else:
                raise ValueError("Empty input file")
        return 0
    except Exception as e:
        print("Error: {}".format(str(e)))


def load_steps_as_x_y(input_file):
    """
    Returns a list of tuples (step_x, step_y)

    :param input_file:
    :type input_file:
    :return:
    :rtype:
    """
    for line in input_file:
        line = line.strip()
        if line:
            items = line.split(' ')
            if len(items) != 2:
                raise ValueError("Wrong number of items: {}.".format(items))

            direction, step_length = items
            step_length = float(step_length)

            if direction in STEP_DIRECTION_X_MAPPING:
                yield (STEP_DIRECTION_X_MAPPING[direction] * step_length), 0
            elif direction in STEP_DIRECTION_Y_MAPPING:
                yield 0, (STEP_DIRECTION_Y_MAPPING[direction] * step_length)
            else:
                raise ValueError("Invalid direction: " + direction)


if __name__ == '__main__':
    sys.exit(main())
