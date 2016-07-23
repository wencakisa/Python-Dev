import requests
import sys
import os

OPENING_SCRIPT_TAG = '<script type="text/javascript">window._sharedData = '
CLOSING_SCRIPT_TAG = '</script>'

OWNER_PREFIX = '"owner": '
USERNAME_PREFIX = '"username": "'
PHOTO_URL_PREFIX = '"display_src": "'

FILENAME_FORMAT = 'Photo_by_{}_{}.jpg'


def main():
    if len(sys.argv) != 3:
        print('Usage: <script> <destination_path> <picture_url>')
        return 1

    destination_path = os.path.expanduser(sys.argv[1])

    if not os.path.isdir(destination_path):
        while True:
            choice = str(input('{} does not exists. Do you want to create it? (Y/n) '.format(destination_path))).lower()

            if choice == 'y':
                os.mkdir(destination_path)
                break
            elif choice == 'n':
                print('Exiting...')
                return 2
            else:
                print('Invalid choice...')

    os.chdir(destination_path)

    original_url = sys.argv[2]

    try:
        resp = requests.get(original_url)
    except ConnectionError:
        print('Invalid URL provided.')
        return 1

    html_code = resp.text

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
    special_id = photo_url[-25: -20]

    filename = FILENAME_FORMAT.format(username, special_id)

    print('Downloading...')

    with open(filename, 'wb') as f:
        f.write(requests.get(photo_url).content)

    print('Photo successfully downloaded in {}'.format(destination_path))

    return 0

if __name__ == '__main__':
    sys.exit(main())
