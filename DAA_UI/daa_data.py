from PyQt5.QtCore import QThread ,  pyqtSignal,  QDateTime , QObject
from PyQt5.QtWidgets import QApplication,  QDialog,  QLineEdit
import sys

class BackendThread(QObject):
    # 通过类成员对象定义信号
    update_date = pyqtSignal(str)
    
    # 处理业务逻辑
    def Info_Display(self):
        while True:
            data = QDateTime.currentDateTime()
            currTime = data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(str(currTime))
            time.sleep(1)