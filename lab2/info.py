import argparse


def input_info() -> argparse.Namespace:
    """
    Считываем аргументы, переданные пользователем через консоль.
    word - слово, по которому будем скачивать изображения
    count - количество изображений
    destination - путь, куда будем скачивать изображения
    annotation - путь, куда будет записана аннотация
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('word', type=str, help='Word')
    parser.add_argument('count', type=int, help='Count images')
    parser.add_argument('destination', type=str, help='Directory to download')
    parser.add_argument('annotation', type=str, help='Annotation file')
    args = parser.parse_args()

    return args