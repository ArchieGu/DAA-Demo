# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'daa_main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,  QDialog,  QLineEdit



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1300, 900)
        Form.setMinimumSize(QtCore.QSize(1300, 900))
        Form.setMaximumSize(QtCore.QSize(1300, 900))
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 861, 896))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(650, 760, 131, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(650, 800, 131, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(650, 840, 131, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 810, 180, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setObjectName("label_8")

        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(220, 810, 180, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_28.setObjectName("label_28")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(740, 80, 100, 671))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setPixmap(QtGui.QPixmap("pic/alt.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(750, 420, 21, 321))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("pic/编组 6.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(120, 130, 600, 600))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("pic/1.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(10, 80, 100, 671))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("pic/编组 7.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(20, 530, 21, 211))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("pic/编组 6.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(385, 50, 72, 681))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("pic/其他.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.frame_2 = QtWidgets.QFrame(Form)

        self.frame_2.setGeometry(QtCore.QRect(870, 0, 421, 485))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 60, 401, 401))
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 141, 41))
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setPixmap(QtGui.QPixmap("pic/7.png"))
        self.label_5.setObjectName("label_5")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(870, 495, 421, 401))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(2)
        self.frame_3.setObjectName("frame_3")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 150, 15))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(250, 20, 120, 15))
        self.label_13.setObjectName("label_13")
        #self.label_14 = QtWidgets.QLabel(self.frame_3)
        #self.label_14.setGeometry(QtCore.QRect(300, 20, 72, 15))
        #self.label_14.setObjectName("label_14")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(190, 240, 41, 20))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("pic/编组 11.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        self.label_17.setGeometry(QtCore.QRect(190, 130, 41, 21))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("pic/编组 12.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_3)
        self.label_18.setGeometry(QtCore.QRect(10, 70, 72, 15))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_3)
        self.label_19.setGeometry(QtCore.QRect(20, 110, 31, 81))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("pic/lingxing1.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame_3)
        self.label_20.setGeometry(QtCore.QRect(20, 210, 31, 81))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("pic/lingxing1.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame_3)
        self.label_21.setGeometry(QtCore.QRect(20, 310, 31, 81))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("pic/lingxing1.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame_3)
        self.label_22.setGeometry(QtCore.QRect(190, 350, 41, 21))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("pic/编组 12.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(340, 60, 41, 41))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("pic/编组 4.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        
        self.label_25 = QtWidgets.QLabel(self.frame_3)
        self.label_25.setGeometry(QtCore.QRect(340, 102, 41, 77))
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("pic/编组 8.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_25")

        self.label_26 = QtWidgets.QLabel(self.frame_3)
        self.label_26.setGeometry(QtCore.QRect(340, 175, 41, 77))
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("pic/编组 8.png"))
        self.label_26.setScaledContents(True)
        self.label_26.setObjectName("label_26")

        self.label_27 = QtWidgets.QLabel(self.frame_3)
        self.label_27.setGeometry(QtCore.QRect(340, 253, 41, 75))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("pic/编组 8.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")


        self.label_23 = QtWidgets.QLabel(self.frame_3)
        self.label_23.setGeometry(QtCore.QRect(340, 360, 41, 31))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("pic/编组 5.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "DAA UI"))
        self.label_4.setText(_translate("Form", "ALT"))
        self.label_6.setText(_translate("Form", "TAS"))
        self.label_7.setText(_translate("Form", "GS"))
        self.label_8.setText(_translate("Form", "Longitude/Latitude"))
        self.label_12.setText(_translate("Form", "ALONG TRACK  50 NM"))
        self.label_13.setText(_translate("Form", "Vertical   1000   FT"))
        #self.label_14.setText(_translate("Form", "TextLabel"))
        self.label_18.setText(_translate("Form", "TextLabel"))
    