import csv
import os


def create_annotation(annotation: str, directory: str) -> None:
    """
    Функция создает аннотацию, создаётся csv файл, записывается заголовок ('Relative path', 'Absolute path') и заносятся относительный и абсолютный пути.
    :param directory: директория с изображениями
    :param annotation:csv файл для аннотации
    :return: None
    """
    with open(annotation, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Relative path', 'Absolute path'])
        for filename in os.listdir(directory):
            rel_path=os.path.relpath(os.path.join(directory,filename))
            abs_path=os.path.abspath(os.path.join(directory,filename))
            writer.writerow([rel_path,abs_path])