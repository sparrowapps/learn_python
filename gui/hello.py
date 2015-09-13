# coding: utf-8

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

from hellowindow import *


class Hello (QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.connect(self.pushButton, SIGNAL("clicked()"), self.btn_clicked)

    def btn_clicked(self):
        text = self.lineEdit.text()
        self.label.setText("hello sparrow word %s" % text)
        

if __name__ == '__main__':
    app =QApplication(sys.argv)
    window = Hello()
    window.show()
    sys.exit(app.exec_())


'''
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic


form_class = uic.loadUiType("hello.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect(self.pushButton, SIGNAL("clicked()"), self.btn_clicked)

    def btn_clicked(self):
        text = self.lineEdit.text()
        self.label.setText("hello world %s" % text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
'''

