import sys
import os
from UI import daa_ui1,daa_ui2,daa_ui2_test

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from BackEnd.backend import backend

class DAA_Form1(QMainWindow):

    def __init__(self, parent=None):
        super(DAA_Form1, self).__init__(parent)
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
        self.ui.label_lon_lat.setStyleSheet("color:white;")
        #self.ui.label_18.setStyleSheet("color:white;")
        self.timer_a = QTimer(self)
        self.timer_a.timeout.connect(self.load_lon_lat())
    
    def start_timer(self):
        self.timer_a.start(500)

    def load_lon_lat(path_lon,path_lat):
        self.ui.label_lon_lat.setText(path_lon,path_lat)
        

class DAA_Form2(QMainWindow):

    def __init__(self, parent=None):
        super(DAA_Form2, self).__init__(parent)
        self.ui = daa_ui2.Ui_Form()
        self.ui.setupUi(self)
        self.ui.label.setStyleSheet("color:white")
        self.ui.frame_1.setStyleSheet("background:black;")
        self.ui.frame_2.setStyleSheet("background:black;")
        self.ui.frame_3.setStyleSheet("background:black;")
        #url = os.getcwd() + '/UI/map_b.html'
        url = 'UI/map_b.html'
        print(url)
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(url))
        self.ui.horizontalLayout.addWidget(self.browser)

if __name__=='__main__':

    app = QApplication(sys.argv)
    backend()
    #form = DAA_Form1()
    #form2 =  DAA_Form2()
    #form.show()
    #form2.show()
    sys.exit(app.exec_())
