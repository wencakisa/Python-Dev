import urllib.request
import os
import platform


def main():
    if platform.system() == 'Windows':
        magic_dir = 'C:\\'
    elif platform.system() == 'Linux':
        magic_dir = os.path.expanduser('~/Pictures/InstaDownloads')
    else:
        raise Exception('OS not supported.')

    req_str = str(input('Enter picture URL: ')).strip()
    f = urllib.request.urlopen(req_str)
    magic_str = ''

    for el in str(f.read().decode('utf-8')).split('\n'):
        if el.strip()[:52] == '<script type="text/javascript">window._sharedData = ':
            magic_str = el.split('"owner": ')[1][:-10]
            break

    if magic_str == '':
        raise Exception('Invalid picture URL.')

    magic_user = magic_str.split('"username": ')[1].split(', ')[0][1:-1]
    magic_url = magic_str.split('"display_src": ')[1].split(', ')[0][1:-1]
    filename = 'Photo_by_{}_{}.png'.format(magic_user, magic_url[-25:-20])

    if not os.access(magic_dir, os.F_OK):
        os.mkdir(magic_dir)

    print('Downloading...')

    os.chdir(magic_dir)
    urllib.request.urlretrieve(magic_url, filename)

    print('Photo successfully downloaded in {}'.format(magic_dir))

if __name__ == '__main__':
    main()
