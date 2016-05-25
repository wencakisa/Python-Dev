import sys


def main():
    try:
        key = int(input())
        msg = str(input())
        print(get_secret_msg(key, msg))
        return 0
    except Exception as e:
        print('INVALID INPUT')


def get_secret_msg(key, msg):
    msg = msg.upper()
    normal_alphabet = ''.join(chr(i) for i in range(65, 91))
    secret_alphabet = normal_alphabet[key:] + normal_alphabet[:key]

    return ''.join(secret_alphabet[normal_alphabet.find(symbol)] if symbol.isalpha() else symbol for symbol in msg)


if __name__ == '__main__':
    sys.exit(main())
