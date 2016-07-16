import sys
import string


def main():
    try:
        key = int(input())
        msg = str(input())

        print(get_secret_msg(key, msg))

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def get_secret_msg(key, msg):
    alphabet = string.ascii_uppercase
    crypt_alphabet = alphabet[key:] + alphabet[:key]

    return ''.join(crypt_alphabet[alphabet.find(symbol)] if symbol.isalpha() else symbol for symbol in msg.upper())


if __name__ == '__main__':
    sys.exit(main())
