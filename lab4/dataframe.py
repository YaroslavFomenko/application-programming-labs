import cv2
import pandas as pd


def get_image_dimensions(path: str) -> tuple:
    '''
    Функция для получения размеров изображения
    :param path: дириктория с изображениями
    :return: высота, ширина, глубина
    '''
    image = cv2.imread(path)
    if image is None:
        return None, None, None
    height, width, depth = image.shape
    return height, width, depth


def add_columns(df: pd.DataFrame) -> None:
    '''
    Добавление столбцов с размерами изображения
    :param df: DataFrame
    '''
    heights, widths, depths = [], [], []
    for path in df['Absolute path']:
        height, width, depth = get_image_dimensions(path)
        heights.append(height)
        widths.append(width)
        depths.append(depth)

    df['height'] = heights
    df['width'] = widths
    df['depth'] = depths


def filter_images(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    '''
    Функция фильтрации изображений
    :param df:
    :param max_width: макс ширин
    :param max_height: макс высота
    :return: pandas DataFrame (object)
    '''
    return df[(df['height'] <= max_height) & (df['width'] <= max_width)]


def add_column_area(df: pd.DataFrame) -> None:
    '''
    Функция добавления столбца area
    :param df: pandas DataFrame (object)
    :return: None
    '''
    df['area'] = df['height'] * df['width']
