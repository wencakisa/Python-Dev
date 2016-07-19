import os
import sys
import logging

# If error occurred, check the error.log file!
logging.basicConfig(filename='error.log', filemode='a', level=logging.DEBUG)


'''
    An implementation of the 'glob' module, but only with 'os' module
'''


def main():
    if len(sys.argv) < 3:
        print('Please provide at least 2 arguments.')
        print('python3 find.py <dir_name> <filename>')
    else:
        paths = find_file(dir_name=sys.argv[1], filename=sys.argv[2])

        if paths:
            print('\n'.join(paths))
        else:
            print('Check error.log')


def is_wildcard(filename):
    """
    Checks whether the file name is wildcard or not
    :param filename: input filename
    :return: bool
    """

    if filename[0] == '*' or filename[-1] == '*':
        return True

    return False


def find_file_with_wildcard(dir_name, filename):
    paths = []

    filename = filename[1:] if filename[0] == '*' else filename[:-1]

    if os.path.exists(dir_name) and os.access(dir_name, os.R_OK):
        for root, dirs, files in os.walk(dir_name):
            for file in files:
                wild_start = file[:len(filename)]
                wild_end = file[len(file) - len(filename):]

                if wild_start == filename or wild_end == filename:
                    paths.append(os.path.join(root, file))

        if paths:
            return paths
        else:
            logging.warning('Files not found.')
    else:
        error_msg = ''

        if not os.path.exists(dir_name):
            error_msg = 'Directory "{}" not found.'.format(dir_name)
        if not os.access(dir_name, os.R_OK):
            error_msg = 'Don`t have permission for "{}"'.format(dir_name)

        logging.warning(error_msg)


def find_file_without_wildcard(dir_name, filename):
    paths = []

    if os.path.exists(dir_name) and os.access(dir_name, os.R_OK):
        for root, dirs, files in os.walk(dir_name):
            if filename in files:
                paths.append(os.path.join(root, filename))

        if paths:
            return paths
        else:
            logging.warning('File "{}" not found.'.format(filename))
    else:
        error_msg = ''

        if not os.path.exists(dir_name):
            error_msg = 'Directory "{}" not found.'.format(dir_name)
        if not os.access(dir_name, os.R_OK):
            error_msg = 'Don`t have permission for "{}"'.format(dir_name)

        logging.warning(error_msg)


def find_file(dir_name, filename):
    if is_wildcard(filename):
        return find_file_with_wildcard(dir_name, filename)
    else:
        return find_file_without_wildcard(dir_name, filename)


if __name__ == '__main__':
    main()
