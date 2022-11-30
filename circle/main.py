import random
import sys
from PyQt5 import uic
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPainter, QPixmap, QPen
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class CircleApp(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint_circle)
        self.setWindowTitle('Circle')
        self._image = QPixmap('background.png')
        self.should_paint_circle = False

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.should_paint_circle:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(QPen(Qt.yellow, 5, Qt.SolidLine))
            radius = random.randint(0, 200)
            a, b = random.randint(0, 700), random.randint(0, 700)
            painter.drawEllipse(a, b, radius, radius)

    def paint_circle(self):
        self.should_paint_circle = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircleApp()
    ex.show()
    sys.exit(app.exec())
