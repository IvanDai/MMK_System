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

class SetInfoWindow(QDialog,setinfo):

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
        if User().db_connect():
            self.user = User(self.usr_id)
            self.label_acc.setText(self.usr_id)
            if self.admin:
                self.label_admin.setText("管理员")
            else:
                self.label_admin.setText("普通用户")
            self.lineEdit.setText(self.user.name)
            self.lineEdit_2.setText(self.user.phone)
            self.lineEdit_3.setText(self.user.email)
            self.pushButton.clicked.connect(self.Set_Pwd)
            self.buttonBox.accepted.connect(self.Save_Changes)
            self.buttonBox.rejected.connect(self.Quit)
        else:
            QMessageBox.information(self,"警告",'请检查数据库连接！',QMessageBox.Ok,QMessageBox.Ok)

    def Set_Pwd(self):
        self.window = SetPwdWindow(self.usr_id)
        self.close()
        self.window.show()
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
        if User().db_connect():
            phone = self.lineEdit_2.text()
            mail = self.lineEdit_3.text()
            if phone and (not re.match("[0-9]{11}",phone)):
                QMessageBox.information(self,"警告",'手机号格式错误！请重新输入！',QMessageBox.Ok,QMessageBox.Ok)
                self.lineEdit_2.setText("")
            # 邮箱格式不对（非必填）
            elif mail and (not re.match(r'^[0-9a-zA-Z_\.]+@[a-zA-Z0-9\.]+\.[a-zA-Z]{2,3}$',mail)):
                QMessageBox.information(self,"警告",'邮箱格式错误！请重新输入！',QMessageBox.Ok,QMessageBox.Ok)
                self.lineEdit_3.setText("")
            else:
                self.user.name  = self.lineEdit.text()
                self.user.phone = phone
                self.user.email = mail
                A = QMessageBox.question(self,'确认','是否确认保存设置？',QMessageBox.Yes | QMessageBox.No)   #创建一个二次确认框
                if A == QMessageBox.Yes:
                    self.user.PushUser()
                self.Quit()
        else:
            QMessageBox.information(self,"警告",'请检查数据库连接！',QMessageBox.Ok,QMessageBox.Ok)
    
class SetPwdWindow(QDialog,setpwd):

    def __init__(self,usr_id):
        QWidget.__init__(self)

        self.usr_id = usr_id
            # 显示窗口
        self.setupUi(self)
        # 设置主题
        self.t = Theme(self)   # 创建主题，t.theme["Theme"]用于存储主题
        self.Handle_Buttons()
        return
    
    def Handle_Buttons(self):
        if User().db_connect():
            self.user = User(self.usr_id)
            self.buttonBox.accepted.connect(self.Save_Pwd)
            self.buttonBox.rejected.connect(self.Quit)
    
    def Quit(self):
        self.window = SetInfoWindow(self.usr_id, self.user.admin)
        self.close()
        self.window.show()
        return
    
    def Save_Pwd(self):
        if User().db_connect():
            new_pwd   = self.lineEdit.text()
            input_pwd = self.lineEdit_2.text()
            pwd       = self.user.pwd
            if not new_pwd:
                QMessageBox.information(self,"警告",'请输入新设置的密码！',QMessageBox.Ok,QMessageBox.Ok) 
            elif input_pwd != pwd:
                QMessageBox.information(self,"警告",'密码输入有误！请重新输入以验证！',QMessageBox.Ok,QMessageBox.Ok) 
            else:
                self.user.pwd = new_pwd
                A = QMessageBox.question(self,'确认','是否确认保存设置？',QMessageBox.Yes | QMessageBox.No)   #创建一个二次确认框
                if A == QMessageBox.Yes:
                    self.user.PushUser()
                QMessageBox.information(self,"提示",'密码修改成功，请重新登录！',QMessageBox.Ok,QMessageBox.Ok) 
                from Login import LogIn
                self.window = LogIn()
                self.close()
                self.window.show()
                
        else:
            QMessageBox.information(self,"警告",'请检查数据库连接！',QMessageBox.Ok,QMessageBox.Ok) 


        


def main():
    app = QApplication(sys.argv)
    window = SetInfoWindow('B18012005',0)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
