import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from random import randint


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("")

        self.trick_button = QPushButton('draw', self)
        self.trick_button.resize(40,40)
        self.trick_button.move(125, 100)
        self.trick_button.clicked.connect(self.paint)
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
        r = randint(0, 255)
        g = randint(0,255)
        b = randint(0, 255)
        pen = QPen(QColor(r, g, b), 3)  # Yellow color, 3px thickness
        painter.setPen(pen)

        # Draw the circle
        center_x = randint(0, 300)
        center_y = randint(0,300)
        radius = randint(0, 50)
        painter.drawEllipse(center_x - radius, center_y - radius, radius * 2, radius * 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
