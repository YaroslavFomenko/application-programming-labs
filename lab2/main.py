from annotation import create_annotation
from download import download_images
from iterator import ImageIterator
from info import input_info


def main():
    try:
        args = input_info()
        word = args.word
        count = args.count
        destination = args.destination
        annotation_file = args.annotation

        download_images(word, count, destination)
        create_annotation(annotation_file, destination)
        iterator = ImageIterator(destination)
        for image in iterator:
            print(image)
    except Exception as ex:
        print("Error: ", ex)


if __name__ == '__main__':
    main()