import requests
import sys
import os


def main():
    destination_path, picture_url = parse_cmd_args()

    create_destination_path(path=destination_path)

    resp_text = get_response_text(url=picture_url)

    owner_info = get_owner_info(response_text=resp_text)

    username = get_username(owner_info=owner_info)

    photo_url = get_photo_url(owner_info=owner_info)
    special_id = photo_url[-25: -20]

    filename = generate_filename(username, special_id)

    download_photo(destination_path, filename, photo_url)

    return 0


def parse_cmd_args() -> tuple:
    if len(sys.argv) != 3:
        print('Usage: <script> <destination_path> <picture_url>')
        sys.exit(1)
    
    return os.path.expanduser(sys.argv[1]), sys.argv[2]


def create_destination_path(path: str) -> None:
    if not os.path.isdir(path):
        while True:
            choice = str(input('{} does not exists. Do you want to create it? (Y/n) '.format(path))).lower()

            if choice == 'y':
                os.mkdir(path)
                break
            elif choice == 'n':
                print('Exiting...')
                sys.exit(1)
            else:
                print('Invalid choice...')

    os.chdir(path)


def get_response_text(url: str) -> str:
    try:
        resp = requests.get(url)
    except ConnectionError:
        print('Invalid URL provided.')
        sys.exit(1)

    return resp.text


def get_owner_info(response_text: str):
    opening_script_tag = '<script type="text/javascript">window._sharedData = '
    closing_script_tag = '</script>'
    owner_prefix = '"owner": '

    opening_script_tag_index = response_text.find(opening_script_tag)

    if opening_script_tag_index == -1:
        print('Invalid Instagram picture URL.')
        sys.exit(1)

    start_info = response_text[opening_script_tag_index + len(opening_script_tag):]

    end_index = start_info.find(closing_script_tag)

    photo_info = start_info[:end_index]

    owner_index = photo_info.find(owner_prefix)
    owner_info = photo_info[owner_index + len(owner_prefix):]

    return owner_info


def get_username(owner_info):
    username_prefix = '"username": "'

    username_start_index = owner_info.find(username_prefix)
    username_end_index = owner_info.find('",', username_start_index)

    username = owner_info[username_start_index + len(username_prefix): username_end_index]

    return username


def get_photo_url(owner_info):
    photo_url_prefix = '"display_src": "'

    photo_url_start_index = owner_info.find(photo_url_prefix)
    photo_url_end_index = owner_info.find('",', photo_url_start_index)

    photo_url = owner_info[photo_url_start_index + len(photo_url_prefix): photo_url_end_index]

    return photo_url


def generate_filename(username, special_id):
    return 'Photo_by_{}_{}.jpg'.format(username, special_id)


def download_photo(destination_path, filename, photo_url):
    print('Downloading...')

    with open(filename, 'wb') as f:
        f.write(requests.get(photo_url).content)

    print('Photo successfully downloaded in {}'.format(destination_path))

if __name__ == '__main__':
    sys.exit(main())
