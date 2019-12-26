import sys
import os
from UI import daa_ui1,daa_ui2,daa_ui2_test

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from BackEnd.backend import backend

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = daa_ui1.Ui_Form()
        self.ui.setupUi(self)
        self.ui.frame.setStyleSheet("background:black;")
        self.ui.frame_2.setStyleSheet("background:black;")
        self.ui.frame_3.setStyleSheet("background:black;")
        self.ui.label_4.setStyleSheet("color:white;")
        self.ui.label_6.setStyleSheet("color:white;")
        self.ui.label_7.setStyleSheet("color:white;")
        self.ui.label_8.setStyleSheet("color:white;")
        self.ui.label_10.setStyleSheet("background: transparent;")
        self.ui.label_12.setStyleSheet("color:white;")
        self.ui.label_13.setStyleSheet("color:white;")
        self.ui.label_14.setStyleSheet("color:white;")
        backend()
        


if __name__=='__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
