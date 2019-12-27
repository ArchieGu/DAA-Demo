import sys
import os
from UI import daa_ui1_new,daa_ui2,daa_ui2_test
from BackEnd.Path.Map.utils import uav_model_init 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from BackEnd.backend import backend

class DAA_Form1(QMainWindow):

    def __init__(self, parent=None):
        super(DAA_Form1, self).__init__(parent)
        self.ui = daa_ui1_new.Ui_Form()
        self.ui.setupUi(self)
        self.ui.frame.setStyleSheet("background:black;")
        self.ui.frame_2.setStyleSheet("background:black;")
        self.ui.frame_3.setStyleSheet("background:black;")
        self.ui.label_4.setStyleSheet("color:white;")
        self.ui.label_16.setStyleSheet("color:white;")
        self.ui.label_17.setStyleSheet("color:white;")
        self.ui.label_6.setStyleSheet("color:white;")
        self.ui.label_7.setStyleSheet("color:white;")
        self.ui.label_8.setStyleSheet("color:white;")
        self.ui.label_10.setStyleSheet("background: transparent;")
        self.ui.label_12.setStyleSheet("color:white;")
        self.ui.label_13.setStyleSheet("color:green;")
        self.ui.label_14.setStyleSheet("color:white;")
        self.ui.label_22.setStyleSheet("color:white;")
        self.ui.label_33.setStyleSheet("color:white;")
        self.ui.label_34.setStyleSheet("color:white;")
        self.ui.label_18.setStyleSheet("color:white;")
        self.ui.label_36.setStyleSheet("color:white;")
        self.ui.label_35.setStyleSheet("color:white;")
        
        self.Ownship = uav_model_init()
        self.path_lon,self.path_lat = backend()
        self.path_lon = self.path_lon.tolist()
        self.path_lat = self.path_lat.tolist()
        self.timer_a = QTimer(self)
        self.timer_a.timeout.connect(self.load_lon_lat)
        self.timer_a.timeout.connect(self.load_lon_lat)
        self.count = 0
        self.start_timer()
    
    def start_timer(self):
        self.timer_a.start(500)
    def stop_timer(self):
        self.timer_a.stop()

    def load_lon_lat(self):
        if self.count > len(self.path_lat):
            self.timer_a.stop()
        else:
            self.ui.label_13.setText(str(self.path_lon[self.count])+' / '+str(self.path_lat[self.count]))
            self.count+=1
    

class DAA_Form2(QMainWindow):

    def __init__(self, parent=None):
        super(DAA_Form2, self).__init__(parent)
        self.ui = daa_ui2.Ui_Form()
        self.ui.setupUi(self)
        self.ui.label.setStyleSheet("color:white")
        self.ui.frame_1.setStyleSheet("background:black;")
        self.ui.frame_2.setStyleSheet("background:black;")
        self.ui.frame_3.setStyleSheet("background:black;")
        
        url = os.getcwd() +r'\UI\map_b.html'
        print(url)
        self.browser = QWebEngineView()
        #self.browser.loadStarted.connect(lambda: print("Loading started"))
        #self.browser.loadProgress.connect(lambda p: print("Loading progress: {}%".format(p)))
        #self.browser.loadFinished.connect(lambda: print("Loading finished"))
        self.browser.load(QUrl.fromLocalFile(url))
        self.browser.show()
        self.ui.horizontalLayout.addWidget(self.browser)

        self.data_ownship = uav_model_init()
        self.path_lon,self.path_lat,self.path_yaw = backend()    
        self.path_lon = self.path_lon.tolist()    # 经度序列
        self.path_lat = self.path_lat.tolist()    # 纬度序列
        self.path_yaw = self.path_yaw.tolist()    # 本机航向角序列

        self.timer_a = QTimer(self)
        self.timer_a.timeout.connect(self.import_info_own)
        self.count = 0
        self.start_timer()
   
    def start_timer(self):
        self.timer_a.start(500)

    def stop_timer(self):
        self.timer_a.stop()

    def import_info_own(self):
      
        if self.count > len(self.path_lat):
            self.timer_a.stop()
        else:
            current_lng = float(self.path_lon[self.count])
            current_lat = float(self.path_lat[self.count])
            current_yaw = float(self.path_yaw[self.count])
            print("current_yaw:",current_yaw)
            js_string_own = '''update_own_position(%f,%f,%f)'''%(current_lng,current_lat,current_yaw-45)
            self.browser.page().runJavaScript(js_string_own)
            self.count+=1
     
 


if __name__=='__main__':

    app = QApplication(sys.argv)
    #form = DAA_Form1()
    form2 =  DAA_Form2()
    #form.show()
    form2.show()
    sys.exit(app.exec_())
