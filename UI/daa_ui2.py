# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'daa_ui2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(981, 662)
        self.frame_1 = QtWidgets.QFrame(Form)
        self.frame_1.setGeometry(QtCore.QRect(0, 0, 981, 71))
        self.frame_1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_1.setLineWidth(2)
        self.frame_1.setObjectName("frame_1")
        self.label = QtWidgets.QLabel(self.frame_1)
        self.label.setGeometry(QtCore.QRect(30, 30, 72, 15))
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 80, 331, 271))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(0, 360, 331, 301))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(2)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(340, 80, 641, 581))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(2)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 641, 581))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "DAA_UI2"))
        self.label.setText(_translate("Form", "TextLabel"))

