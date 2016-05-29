import sys


def main():
    try:
        input_filename = str(input())
        word_to_search = str(input())
        input_data = load_input_data(input_filename)
        anagrams = get_anagrams(input_data, word_to_search)
        print_anagrams(anagrams)
        return 0
    except Exception:
        print('INVALID INPUT')


def load_input_data(input_filename):
    with open(input_filename, encoding='utf-8') as f:
        return [line.strip() for line in f]


def get_anagrams(input_data, word_to_search):
    return [
        word for word in input_data
        if ''.join(sorted(word)) == ''.join(sorted(word_to_search)) and word != word_to_search
    ]


def print_anagrams(anagrams):
    [print(anagram) for anagram in sorted(anagrams)] if anagrams else print('NO ANAGRAMS')

if __name__ == '__main__':
    sys.exit(main())
