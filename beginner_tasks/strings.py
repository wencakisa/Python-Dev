def slice(string, max_length):
    if max_length < len(string):
        return string[:max_length] + "..."

    return string


def show_after(string, after):
    to_return = ""

    string = string.split(' ')

    for i in range(len(string)):
        if string[i] == after:
            string = string[i + 1:len(string)]
            break

    for word in string:
        to_return += word + " "

    return to_return


def show_after_2(string, after):
    to_return = ""

    if after in string:
        for i in range(string.find(after), len(string)):
            to_return += string[i]

    return to_return


def main():
    string = "This is soo difficult, I prefer playing WoW"
    after = "is"
    print(show_after(string, after))


if __name__ == '__main__':
    main()
