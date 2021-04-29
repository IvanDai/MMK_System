import sys,os
import re
from PyQt5.uic import loadUiType
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from db_User import *
from db_ClassRoom import *
from db_Event import *

from SetTheme import *

setinfo,_ = loadUiType('../ui/SetInfo.ui')
setpwd,_  = loadUiType('../ui/SetPwd.ui')

class Set_Info_Window(QDialog,setinfo):

    def __init__(self,usr_id,admin):
        QWidget.__init__(self)

        self.usr_id = usr_id
        self.admin  = admin
        # 显示窗口
        self.setupUi(self)
        # 设置主题
        self.t = Theme(self)   # 创建主题，t.theme["Theme"]用于存储主题
        self.Handle_Buttons()

    def Handle_Buttons(self):
        self.user = User(self.usr_id)
        self.label_acc.setText(self.usr_id)
        if self.admin:
            self.label_admin.setText("管理员")
        else:
            self.label_admin.setText("普通用户")
        self.pushButton.clicked.connect(self.Set_Pwd)
        self.buttonBox.accepted.connect(self.Save_Changes)
        self.buttonBox.rejected.connect(self.Quit)

    def Set_Pwd(self):
        return
    
    def Quit(self):
        if not self.admin:
            from UserApp import UserApp
            self.window = UserApp(self.usr_id)
            self.close()
            self.window.show()
        # else:
        #     from AdminApp import AdminApp
        #     self.window = AdminApp(self.usr_id)
        #     self.close()
        #     self.window.show()
    
    def Save_Changes(self):
        self.user.name  = self.lineEdit.Text()
        self.user.phone = self.lineEdit_2.Text()
        self.user.email = self.lineEdit_3.Text()

            
