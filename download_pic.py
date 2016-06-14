import urllib.request
import sys
import os
import platform


def main():
    if platform.system() == 'Windows':
        magic_dir = 'D:\Pictures\Instagram'
    elif platform.system() == 'Linux':
        magic_dir = '/home/wencakisa/Pictures/Instagram/'
    else:
        raise Exception('OS not supported.')

    req_str = sys.argv[1]
    f = urllib.request.urlopen(req_str)
    magic_str = ''

    for el in str(f.read().decode('utf-8')).split('\n'):
        if el.strip()[:52] == '<script type="text/javascript">window._sharedData = ':
            magic_str = el.split('"owner": ')[1][:-10]

    magic_user = magic_str.split('"username": ')[1].split(', ')[0][1:-1]
    magic_url = magic_str.split('"display_src": ')[1].split(', ')[0][1:-1]
    filename = 'Photo_by_{}_{}.png'.format(magic_user, magic_url[-25:-20])

    os.chdir(magic_dir)
    urllib.request.urlretrieve(magic_url, filename)

    print('Photo successfuly saved in {}'.format(magic_dir))

if __name__ == '__main__':
    main()
