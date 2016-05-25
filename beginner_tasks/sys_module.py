import sys
import os


def main():
    print(sys.platform)
    print(sys.version)
    print(sys.argv)
    print(os.path.getsize('./csv_task/file_tasks/catalog_full.csv'))
    print(os.path.isfile('./csv_task/file_tasks/catalog_full.csv'))
    print(os.path.isfile('./csv_task/file_tasks/'))
    print(os.path.isdir('./csv_task/file_tasks/'))
    print(os.path.exists('./csv_task/file_tasks/hello'))
    print(os.path.exists('./csv_task/file_tasks/'))
    print(os.path.dirname('./csv_task/file_tasks/catalog_full.csv'))
    print(os.path.basename('./csv_task/file_tasks/catalog_full.csv'))

if __name__ == '__main__':
    main()
