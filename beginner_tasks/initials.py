def get_initials(name):
    name = name.split()

    initials_list = [
        name[i][0]
        for i in range(len(name))
        if name[i][0].isupper()
    ]

    return '.'.join(initial for inital in initials_list)


def main():
    me = 'Vencislav Naydenov Tasheff'
    dutch = 'Guido van Rossum'
    german = 'Werher von Braun'

    print(get_initials(me))
    print(get_initials(dutch))
    print(get_initials(german))

if __name__ == '__main__':
    main()
