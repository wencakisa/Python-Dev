import requests
import os
import platform
import sys

OPENING_SCRIPT_TAG = '<script type="text/javascript">window._sharedData = '
CLOSING_SCRIPT_TAG = '</script>'
OWNER_PREFIX = '"owner": '
USERNAME_PREFIX = '"username": "'
PHOTO_URL_PREFIX = '"display_src": "'
FILENAME_FORMAT = 'Photo_by_{}_{}.jpg'


def main():
    if platform.system() == 'Windows':
        directory = 'D:\\'
    elif platform.system() == 'Linux':
        directory = os.path.expanduser('~/Pictures/InstaDownloads')
    else:
        raise Exception('OS not supported.')

    original_url = str(input('Enter picture URL: ')).strip()
    f = requests.get(original_url)
    html_code = f.text

    start_index = html_code.find(OPENING_SCRIPT_TAG)

    if start_index == -1:
        print('Invalid Instagram picture URL.')
        return 1

    start_info = html_code[start_index + len(OPENING_SCRIPT_TAG):]

    end_index = start_info.find(CLOSING_SCRIPT_TAG)

    photo_info = start_info[:end_index]

    owner_index = photo_info.find(OWNER_PREFIX)
    owner_info = photo_info[owner_index + len(OWNER_PREFIX):]

    username_start_index = owner_info.find(USERNAME_PREFIX)
    username_end_index = owner_info.find('",', username_start_index)

    username = owner_info[username_start_index + len(USERNAME_PREFIX): username_end_index]

    photo_url_start_index = owner_info.find(PHOTO_URL_PREFIX)
    photo_url_end_index = owner_info.find('",', photo_url_start_index)

    photo_url = owner_info[photo_url_start_index + len(PHOTO_URL_PREFIX): photo_url_end_index]
    special_id = photo_url[-25:-20]

    filename = FILENAME_FORMAT.format(username, special_id)

    if not os.access(directory, os.F_OK):
        os.makedirs(directory)
        
    os.chdir(directory)

    print('Downloading...')

    with open(filename, 'wb') as f:
        f.write(requests.get(photo_url).content)

    print('Photo successfully downloaded in {}'.format(directory))

if __name__ == '__main__':
    sys.exit(main())
