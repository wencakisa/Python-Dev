import sys
from urllib.parse import urlparse
from collections import defaultdict

URL_PREFIX = 'url="'
RESP_T_PREFIX = 'resp_t="'


def main():
    try:
        input_filename = str(input())
        input_data = load_data(input_filename)
        important_data = get_important_data(input_data)
        slowest_page_info = get_slowest_page(important_data)
        print('\n'.join(map(str, slowest_page_info)))
    except Exception:
        print('INVALID INPUT')


def load_data(input_filename):
    with open(input_filename, encoding='utf-8') as f:
        return [line.split(' ') for line in f]


def get_important_data(input_data):
    all_urls = []
    resp_times = []

    for data in input_data:
        for element in data:
            if not element.find(URL_PREFIX):
                all_urls.append(urlparse(element[element.find(URL_PREFIX) + len(URL_PREFIX): -1]))
            elif not element.find(RESP_T_PREFIX):
                resp_times.append(float(element[element.find(RESP_T_PREFIX) + len(RESP_T_PREFIX): -1]))

    valid_urls = []

    for url in all_urls:
        if url.path[-4:] != '/ws/':
            valid_urls.append(url.path)
        else:
            del resp_times[all_urls.index(url)]

    important_data = defaultdict(list)

    for i in range(len(valid_urls)):
        important_data[valid_urls[i]].append(resp_times[i])

    for url in important_data.keys():
        important_data[url] = round(sum(important_data[url]) / len(important_data[url]), 3)

    return important_data


def get_slowest_page(important_data):
    slowest_resp_t = max(important_data.values())

    for url, resp_t in important_data.items():
        if resp_t == slowest_resp_t:
            return url, resp_t


if __name__ == '__main__':
    sys.exit(main())
