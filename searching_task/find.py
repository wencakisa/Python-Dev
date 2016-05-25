import os
import sys
import logging

# If error occured, check the error.log file!
logging.basicConfig(filename='error.log', filemode='a', level=logging.DEBUG)


# Checks whether the file name is wildcard or not
def is_wildcard(filename):
    if filename[0] == '*' or filename[-1] == '*':
        return True

    return False


def find_file_with_wildcard(dir_name, filename):
    paths = []

    # Slicing the file name so there is no '*' in it
    if filename[0] == '*':
        # If it starts with '*' -> slice it from 1 to the end
        filename = filename[1: len(filename)]
        # Example: pic* -> pic
    else:
        # If it ends with '*' -> slice it from 0 to the end - 1
        filename = filename[0:-1]
        # Example: *pic -> pic

    # Checks if the dir_name param is a valid dir_name
    if os.path.exists(dir_name) and os.access(dir_name, os.R_OK):
        for root, dirs, files in os.walk(dir_name):
            for file in files:
                # If our file starts or ends with the wildcard:

                # Slice from 0 to the length of our wildcard
                wild_start = file[0: len(filename)]
                # Magic slice!
                wild_end = file[len(file) - len(filename):]

                if wild_start == filename or wild_end == filename:
                    paths.append(os.path.join(root, file))

        # If the file exists somewhere:
        # -> Return the list of (paths, occurences)
        if paths:
            return paths
        # Otherwise:
        # -> Write in the log file that files with this wildcard do not exist.
        else:
            msg = 'Files not found.'
            logging.warning(msg)
            print(msg)
    # If the dir_name param is not a valid dir_name:
    # -> Write in the log file that this dir_name does not exist.
    else:
        if not os.path.exists(dir_name):
            msg = 'Directory "{}" not found.'.format(dir_name)
            logging.warning(msg)
            print(msg)
        if not os.access(dir_name, os.R_OK):
            msg = 'Don`t have permission for "{}"'.format(dir_name)
            logging.warning(msg)
            print(msg)


def find_file_without_wildcard(dir_name, filename):
    paths = []

    # If the dir_name param is a valid dir_name:
    if os.path.exists(dir_name) and os.access(dir_name, os.R_OK):
        for root, dirs, files in os.walk(dir_name):
            if filename in files:
                paths.append(os.path.join(root, filename))

        # If the file exists somewhere:
        # -> Return the list of paths
        if paths:
            return paths
        # Otherwise:
        # -> Write in the log file that file does not exist.
        else:
            msg = 'File "{}" not found.'.format(filename)
            logging.warning(msg)
            print(msg)
    # If the dir_name param is not a valid dir_name:
    # -> Write in the log file that this dir_name does not exist.
    else:
        if not os.path.exists(dir_name):
            msg = 'Directory "{}" not found.'.format(dir_name)
            logging.warning(msg)
            print(msg)
        if not os.access(dir_name, os.R_OK):
            msg = 'Don`t have permission for "{}"'.format(dir_name)
            logging.warning(msg)
            print(msg)


def find_file(dir_name, filename):
    if is_wildcard(filename):
        return find_file_with_wildcard(dir_name, filename)
    else:
        return find_file_without_wildcard(dir_name, filename)


def print_paths(paths):
    if paths:
        for path in paths:
            print(path)
    else:
        print('Check error.log')


def main():
    if len(sys.argv) < 3:
        print('Please provide at least 2 arguments.')
        print('python3 find.py <dir_name> <filename>')
    else:
        paths = find_file(dir_name=sys.argv[1], filename=sys.argv[2])
        print_paths(paths)


if __name__ == '__main__':
    main()
