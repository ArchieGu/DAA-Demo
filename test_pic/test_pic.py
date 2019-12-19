import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random
class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()
        self.resize(500, 500)
        self.setWindowTitle("label显示图片")

        self.label1 = QLabel(self)
        #self.label1.setText("显示图片A")
        self.label1.setFixedSize(378, 378)
        self.label1.move(100, 100)
        self.label1.setStyleSheet("QLabel{background:gray;}")

        self.label2 = QLabel(self)
        #self.label2.setText("显示图片B")
        self.label2.setFixedSize(28, 28)
        self.label2.move(200, 300)
        self.label2.setStyleSheet("QLabel{background:gray;}")
        random_pic = QPixmap('pic/airport.png')
        self.label2.setPixmap(random_pic)


        btn1 = QPushButton(self)
        btn1.setText("开始")
        btn1.move(10, 30)
        btn1.clicked.connect(self.start_timer)

        btn2 = QPushButton(self)
        btn2.setText("停止")
        btn2.move(200, 30)
        btn2.clicked.connect(self.stop_timer)
        self.timer_a = QTimer(self)
        self.timer_a.timeout.connect(self.start_loadPic)
        self.count = 0

    def start_timer(self):
        self.timer_a.start(1000)

    def stop_timer(self):
        self.timer_a.stop()
        pic1 = QPixmap('测试/ss_rotate0.png')
        self.label1.setPixmap(pic1)

    def start_loadPic(self):
        #random_num = random.randint(0,359)
        if self.count>=360:
            self.timer_a.stop()
        else:
            str_pic = '测试/ss_rotate'+str(self.count)+'.png'
            print(str_pic)
            random_pic = QPixmap(str_pic)
            self.label1.setPixmap(random_pic)
            self.count+=1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()
    sys.exit(app.exec_())
