from PyQt5.QtWidgets import QApplication, QGridLayout, QMainWindow, QDesktopWidget, QWidget, QPushButton, QLineEdit,QLabel,QDialog
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Register import *
from Login import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    LogUI = LoginUI()
    LogUI.show()
    
    app.exec_()