from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Register import *
from LoginV2 import *
import time

if __name__ == '__main__':
    UI =  QApplication(sys.argv)
    w = LoginUI()
    w.show()
    UI.exec_()
    time.sleep(0.5)
    result = 10086
    if  result == 10086:
        with open('cache.txt','r') as f:
            line = f.readline()
        
        username = line[:9]
        user_status = int(line[9])
        admin_status = int(line[-1])

        # 开启登录窗口
        EXIT_CODE_REBOOT = result
        if user_status is 1 and admin_status is 0:
            print(user_status)
            print(admin_status)
            # 用户端
            while EXIT_CODE_REBOOT == 10086:
                print(1)
                UIS = QApplication(sys.argv)
                studentWin = Ui_Form(username)
                studentWin.show()
                EXIT_CODE_REBOOT = UIS.exec_()
                studentWin = None
        elif user_status is 0 and admin_status is 1:
            # 管理端
            while EXIT_CODE_REBOOT == 10086:
                UIA = QApplication(sys.argv)
                print(5)
                adminWin = AdminUI(username)
                print(8)
                adminWin.show()
                print(EXIT_CODE_REBOOT)
                EXIT_CODE_REBOOT = UIA.exec_()
                print(EXIT_CODE_REBOOT)
                adminWin = None