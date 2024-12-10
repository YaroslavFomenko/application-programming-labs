from icrawler.builtin import BingImageCrawler


def download_images(word: str, count: int, destination: str) -> None:
    """
    Скачивание изображений
    :word - ключевое слово для скачивания
    :count - количество изображений
    :destination - путь, по которому скачиваются изображения
    """
    try:
        bing_crawler = BingImageCrawler(storage={'root_dir': destination})
        bing_crawler.crawl(keyword=word, max_num=count)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
