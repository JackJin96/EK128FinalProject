

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from functools import partial
#from qtfile import Ui_MainWindow

qtCreatorFile = "Game.ui"  # Enter UI file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

listT = []

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Dot1.clicked.connect(partial(self.pushed, self.Dot1))
        self.Dot2.clicked.connect(partial(self.pushed, self.Dot2))
        self.Dot3.clicked.connect(partial(self.pushed, self.Dot3))
    #def mousePressEvent(self, QMouseEvent):
        #print(QMouseEvent.pos())


        #print(btn.pos())

    def pushed(self, btn):
        t = (btn.x(), btn.y())
        self.Shape_name.setText(str(t))
        if t not in listT and len(listT) < 2:
            listT.append(t)
        if len(listT) == 2:
            self.update()     #somthing's wrong with this update method
                            #Don't know how to clear listT every time

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp, listT)
        qp.end()

    def drawLines(self, qp, coordList):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        if len(listT) == 2:
            qp.drawLine(coordList[0][0], coordList[0][1], coordList[1][0], coordList[1][1])
            qp.drawLine(150,150,250,250)
        else:
            qp.drawLine(100,100,200,200)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
