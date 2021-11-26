import random
import sys

from PyQt5 import uic
from UI import Ui_MainWindow
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.qp = QPainter()
        self.status = 0
        self.pushButtonpushButton.clicked.connect(self.paint)

    def painter(self):
        r = random.randint(10, 200)
        coord = [random.randint(0, 800 - r), random.randint(0, 600 - r)]
        self.qp.begin(self)
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(*coord, r, r)
        self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
