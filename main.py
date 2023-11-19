import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
from PyQt5 import QtCore
from PyQt5.QtGui import QMovie
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor, QPolygon
from random import randint
import graphics


class Main(QMainWindow, graphics.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.data = []
        self.setupUi(self)
        self.initialize_dependencies()

    def initialize_dependencies(self):
        self.pushButton.clicked.connect(self.start)

    def start(self):
        self.paint(randint(1, 838), randint(1, 640), '')

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self, x, y, btn):
        self.x = x
        self.y = y
        self.btn = btn
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        the_storona = randint(20, 250)
        self.data.append([self.x, self.y, the_storona, [randint(0, 255), randint(0, 255), randint(0, 255)]])
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        for dat in self.data:
            qp.setBrush(QColor(dat[-1][0], dat[-1][1], dat[-1][2]))
            x_sd = dat[2] // 2
            y_sd = dat[2] // 2
            qp.drawEllipse(dat[0] - x_sd, dat[1] - y_sd, dat[2], dat[2])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
