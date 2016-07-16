import sys
import iso8601
from collections import defaultdict


def main():
    try:
        input_filename = input()

        cities, cities_by_date = load_data(input_filename)

        if not cities or not cities_by_date:
            raise ValueError('Empty file provided')

        result = []

        for d, cities_for_date in cities_by_date.items():
            missing_cities = cities.difference(cities_for_date)

            if missing_cities:
                result.append((d, ','.join(sorted(missing_cities))))

        if result:
            result.sort()

            for d, cities in result:
                print('{},{}'.format(d.isoformat(), cities))
        else:
            print('ALL DATA AVAILABLE')

        return 0

    except Exception:
        print('INVALID INPUT')
        return 1


def load_data(input_filename):
    with open(input_filename, encoding='utf-8') as f:
        cities = set()
        cities_by_date = defaultdict(set)

        for line in f:
            line = line.strip()

            if line:
                date_str, city_name, *_ = line.split(',')
                cities.add(city_name)
                d = iso8601.parse_date(date_str).date()
                cities_by_date[d].add(city_name)

        return cities, cities_by_date


if __name__ == '__main__':
    sys.exit(main())
