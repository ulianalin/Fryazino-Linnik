import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush
from PyQt6.QtWidgets import QApplication, QMainWindow
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        painter = QPainter(self)
        pen = QPen(QColor(255, 255, 0), 3)  # Yellow color, 3px thickness
        painter.setPen(pen)

        # Draw the circle
        center_x = randint(0, 500)
        center_y = randint(0,300)
        radius = randint(0, 50)
        painter.drawEllipse(center_x - radius, center_y - radius, radius * 2, radius * 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())