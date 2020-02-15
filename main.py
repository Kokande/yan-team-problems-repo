from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import requests
from PyQt5 import uic


API = "http://static-maps.yandex.ru/1.x/"


class Problem(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.initUI()

    def initUI(self):
        self.update_b.clicked.connect(self.update_map)

    def update_map(self):
        pass


if __name__ == '__main__':
    app = QApplication([])
    ex = Problem()
    ex.show()
    sys.exit(app.exec())
