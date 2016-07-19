import re


def slice_str(string, max_length):
    if max_length < len(string):
        return string[: max_length] + "..."

    return string


def show_after(string, after):
    return string[re.search(r'\s{}\s'.format(after), string).span()[1]:]


def main():
    string = "This is soo difficult, I prefer playing WoW"
    after = "is"
    print(show_after(string, after))


if __name__ == '__main__':
    main()
