import argparse
import re


def parsing() -> argparse.Namespace:
    '''
    парсинг аргументов
    :return:Название файла и имя для подсчета
    '''
    parser = argparse.ArgumentParser(description='Подсчет людей по имени в файле.')
    parser.add_argument('filename', type=str, help='Имя файла с анкетами')
    parser.add_argument('name', type=str, help='Имя для подсчета')
    return parser.parse_args()


def read_file(filename: str) -> str:
    '''
    чтение файла
    '''
    try:
        file = open(filename, 'r', encoding="UTF8")
        data = file.read()
        file.close()
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f'Файл {filename} не найден.')


def find_people_by_name(filename: str , name: str ) -> int:
    '''
    поиск количесво людей с заданным именем
    :param filename: исходный файл
    :param name: заданное имя
    :return: количество повторений заданного имени
    '''

    matches = re.findall(f'Имя: {name}', filename)
    count = len(matches)
    return count


def main()-> None:
    try:
        args = parsing()
        filename = read_file(args.filename)
        result = find_people_by_name(filename, args.name)
        print(f"Количество людей с именем '{args.name}': {result}")
    except Exception as e:
        print(f'Произошла ошибка: {e}')


if __name__ == "__main__":
    main()