from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys

class logUI(QDialog):
    def __init__(self):
        super(logUI,self).__init__()
        self.setFixedSize(500,300)
        self.setWindowTitle('管理操作日志')
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        self.log_list = QListWidget()
        layout.addWidget(self.log_list,0,0)
        self.setLayout(layout)
        with open('log.txt','r') as f:
            lines = f.readlines()
            for i in lines:
                item = QListWidgetItem(i)
                self.log_list.addItem(item)
        

if __name__ == '__main__':
    app = QApplication([])
    w = logUI()
    w.exec()