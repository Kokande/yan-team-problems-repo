from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
import sys
import requests
from PyQt5 import uic
import os


API = "http://static-maps.yandex.ru/1.x/"


class Problem(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.update_map()
        self.initUI()

    def initUI(self):
        self.update_b.clicked.connect(self.update_map)

    def update_map(self):
        params = {
            'z': self.z.value(),
            'll': ','.join([self.longitude.text(), self.lattitude.text()]),
            'l': 'map'
        }
        response = requests.get(API, params=params)
        if response:
            with open("map.png", 'wb') as img:
                img.write(response.content)
            self.map.setPixmap(QPixmap("map.png"))

    def closeEvent(self, *args, **kwargs):
        os.remove("map.png")


if __name__ == '__main__':
    app = QApplication([])
    ex = Problem()
    ex.show()
    sys.exit(app.exec())
