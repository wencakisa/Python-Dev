def similarities(first, second):
    return set(first).intersection(set(second))


def main():
    ivan = ['pushene', 'piene', 'tiq tri neshta', 'koli', 'facebook', 'igri']
    maria = ['piene', 'seks', 'pushene', 'shoping']

    print(similarities(ivan, maria))


if __name__ == '__main__':
    main()
