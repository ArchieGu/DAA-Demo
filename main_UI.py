import sys
import os
import json
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
        self.ui.comboBox_2.setStyleSheet("color:white;")
        self.ui.comboBox.setStyleSheet("color:white;")
        self.ui.label_37.setStyleSheet("color:white;")
        self.ui.label_38.setStyleSheet("color:white;")
        self.ui.label_39.setStyleSheet("color:white;")
        self.ui.label_40.setStyleSheet("color:white;")
        self.ui.label_41.setStyleSheet("color:white;")
        self.ui.label_42.setStyleSheet("color:white;")
        self.ui.label_43.setStyleSheet("color:white;")
        self.ui.label_44.setStyleSheet("color:white;")
        self.ui.label_45.setStyleSheet("color:white;")



        self.Ownship = uav_model_init()
        self.alt = self.Ownship.alt
        self.speed = self.Ownship.speed
        self.heading = round(float(self.Ownship.heading) + 360.0,1)

        self.ui.label_3.setPixmap(QPixmap("UI\compass/"+str(self.heading)+'.png'))
        self.ui.label_16.setText(str(self.alt)+'ft')
        self.ui.label_17.setText(str(self.speed)+'m/s')

        self.path_lon,self.path_lat,self.path_yaw = backend()
        self.path_lon = self.path_lon.tolist()
        self.path_lat = self.path_lat.tolist()
        self.timer_a = QTimer(self)
        self.timer_a.timeout.connect(self.load_lon_lat)
        self.timer_a.timeout.connect(self.load_lon_lat)
        self.count = 0
        self.start_timer()
    
    def start_timer(self):
        self.timer_a.start(2000)
    def stop_timer(self):
        self.timer_a.stop()

    def load_lon_lat(self):
        if self.count > len(self.path_lat)-1:
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
        
        url = os.getcwd() +r'\map_gd.html'
        #print(url)
        self.browser = QWebEngineView()
        self.browser.load(QUrl('http://127.0.0.1:9099/map_gd'))
        #self.browser.load(QUrl.fromLocalFile(url))
        self.browser.show()
        self.ui.horizontalLayout.addWidget(self.browser)
        
        '''
        self.data_ownship = uav_model_init()
        self.path_lon,self.path_lat,self.path_yaw = backend()    
        self.path_lon = self.path_lon.tolist()    # 经度序列
        self.path_lat = self.path_lat.tolist()    # 纬度序列
        self.path_yaw = self.path_yaw.tolist()    # 本机航向角序列
        #self.timer_a = QTimer(self)
        
        #self.timer_a.timeout.connect(self.initOwnshipData)
        #self.count = 0
        #self.start_timer()
        '''
    '''
    def start_timer(self):
        self.timer_a.start(500)

    def stop_timer(self):
        self.timer_a.stop()

    def getPathData(self):
        ownship_ID = self.data_ownship.ID
        path_own_list = [] #本机航路序列
        path_data = {}
        for i in range(len(self.path_lon)):
            lng = self.path_lon[i]
            lat = self.path_lat[i]
            path_own_list.append([lng,lat])
            #lng = hanglu_own['point'+str(i)][1]
            #lat = hanglu_own['point'+str(i)][2]
            #hanglu_own_list.append([lng,lat])
        path_data = {
            "name" : ownship_ID,
            "path" : path_own_list
        }
        path2 = json.dumps([path_data])
        with open('static\path2.json','w') as json_file:
            json_file.write(path2)
    '''

if __name__=='__main__':

    app = QApplication(sys.argv)
    form = DAA_Form1()
    form2 =  DAA_Form2()
    form.show()
    form2.show()
    sys.exit(app.exec_())
