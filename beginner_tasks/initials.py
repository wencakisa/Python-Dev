def get_initials(name):
    name = name.split()

    initials_list = [
        name[i][0] for i in range(len(name)) if name[i][0].isupper()
    ]

    initials = ''

    for initial in initials_list:
        initials += initial + '.'

    return initials


def main():
    me = 'Vencislav Naydenov Tasheff'
    dutch = 'Guido van Rossum'
    german = 'Werher von Braun'

    print(get_initials(me))
    print(get_initials(dutch))
    print(get_initials(german))

if __name__ == '__main__':
    main()
