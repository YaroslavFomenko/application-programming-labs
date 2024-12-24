import sys
import os

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
)

from iterator import ImageIterator

OPEN_DATASET_TEXT = "Open dataset."
NEXT_IMG_TEXT = 'Press "Next img" to continue viewing.'


class MyWindow(QWidget):
    def __init__(self):
        """
        Иницализация окна приложения
        """
        super().__init__()
        self.iterator = None
        self.path = None

        # Initialize attributes
        self.open_btn = QPushButton("Open annotation-file")
        self.next_btn = QPushButton("Next img")
        self.image_label = QLabel(OPEN_DATASET_TEXT)
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.init_ui()

    def init_ui(self) -> None:
        """
        Настройки интерфейса
        """
        self.setGeometry(200, 100, 650, 600)
        self.setFixedSize(650, 600)
        self.setWindowTitle("Turtle")

        self.next_btn.setEnabled(False)
        self.image_label.setScaledContents(True)

        self.hbox.addWidget(self.open_btn)
        self.hbox.addWidget(self.next_btn)

        self.vbox.addStretch(1)
        self.vbox.addWidget(self.image_label)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)

        self.open_btn.clicked.connect(self.open_annotations)
        self.next_btn.clicked.connect(self.show_next_img)

    def open_annotations(self) -> None:
        """
        Загружает файл аннотации и передает его итератору
        """
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл аннотаций", "", "Text Files (*.csv)", options=options)
        if file_name:
            try:
                self.iterator = ImageIterator(file_name)
                self.next_btn.setEnabled(True)
                self.show_next_img()
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить файл аннотаций: {e}")

    def show_next_img(self) -> None:
        """
        Отображение следующего изображения
        """
        if self.iterator:
            try:
                self.path = next(self.iterator)
                if not os.path.isfile(self.path):
                    raise FileNotFoundError(f"Изображение {self.path} не найдено.")
                pixmap = QPixmap(self.path)
                if pixmap.isNull():
                    raise ValueError("Изображение не может быть загружено.")
                self.image_label.setPixmap(pixmap)
            except (ValueError, FileNotFoundError) as e:
                QMessageBox.information(self, "Error", str(e))
            except StopIteration:
                self.end_of_images()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ошибка: {e}")

    def end_of_images(self) -> None:
        """
        конец изображений
        """
        if not self.path:
            self.image_label.setText("Список изображений пуст.")
            self.next_btn.setEnabled(False)
            return

        reply = QMessageBox.question(self, "Конец", "Изображения закончились. Хотите начать заново?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.iterator.reset()
            self.show_next_img()
        else:
            self.image_label.setText(OPEN_DATASET_TEXT)
            self.next_btn.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())