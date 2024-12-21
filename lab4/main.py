import argparse

import pandas as pd
import matplotlib.pyplot as plt

from dataframe import add_column_area, add_columns, filter_images


def parse_arguments() -> argparse.Namespace:

    parser = argparse.ArgumentParser(description="Работа с изображением")
    parser.add_argument('path_to_csv_file', type=str, help='path to the csv file')
    args = parser.parse_args()
    return args


def create_histogram(col: pd.Series, x_label: str, plot_label: str) -> None:
    """
    Функция создания гистограммы распределения площади изображений
    :param df: pandas DataFrame (object)
    :return: None
    """
    plt.hist(col, bins=10, edgecolor='black')
    plt.title(plot_label)
    plt.xlabel(x_label)
    plt.ylabel('Количество изображений')
    plt.show()


def main():
    args = parse_arguments()
    try:
        df = pd.read_csv(args.path_to_csv_file)
        print(df.head())
        add_columns(df)
        print(df.head())
        stats = df[['height', 'width', 'depth']].describe()
        print(stats)

        filtered_df = filter_images(df, 500, 500)
        print(filtered_df.head())

        add_column_area(df)
        print(df.head())

        df_sort = df.sort_values(by='area')
        print(df_sort.head())

        create_histogram(df['area'], "Площадь" ,"Распределение площадей")
        print("Гистограмма выведена")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
