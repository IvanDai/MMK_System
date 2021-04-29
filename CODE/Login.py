# -*- coding: UTF-8 -*-
import sys,os
import re
import time
from PyQt5.uic import loadUiType
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from UserApp import *
from db_User import *
from Login import *

login,_     = loadUiType('../ui/Login.ui')
signup,_    = loadUiType('../ui/SignUp.ui')


class LogIn(QWidget , login):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        # 设置主题
        Theme(self)
        self.Handle_Buttons()
    
    def Handle_Buttons(self):
        self.pushButton.clicked.connect(self.Sign_Up)
        self.pushButton_2.clicked.connect(self.Sign_In)
        self.lineEdit_2.returnPressed.connect(self.Sign_In)
    
    def Sign_Up(self):
        self.su_window = SignUp()
        self.close()
        self.su_window.show()

    def Sign_In(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        self.label_notice.setText("")

        if User().db_connect():                           # 数据库链接情况判断，确保数据库正常打开，不然会闪退
            current_user = User(username)                 # 创建账户实例，检测是否存在账户
            if current_user.PullUser():
                if password == current_user.pwd:
                    # 登录到主界面
                    if not int(current_user.admin):
                        from UserApp import UserApp
                        self.si_window = UserApp(current_user.id)
                        self.close()
                        time.sleep(0.5)
                        self.si_window.show()
                    # else:
                    #     self.si_window = AdminApp(current_user.id)
                    #     self.close()
                    #     self.si_window.show()
                    print('登陆成功')
                else:
                    self.lineEdit_2.setText("")
                    self.label_3.setText("密码错误，请重新输入！") # 窗口内部提示
            else:
                self.label_notice.setText("请确保账号已注册！")
        else:
            self.label_notice.setText("ERROR:请检查数据库链接！") 


class SignUp(QWidget ,signup):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        Theme(self)
        self.Handle_Buttons() 
    
    def Handle_Buttons(self):
        self.buttonBox.accepted.connect(self.Register_Acc)
        self.buttonBox.rejected.connect(self.Quit_Register)
    
    def Quit_Register(self):
        self.login_window = LogIn()
        self.close()
        self.login_window.show()
    
    def Register_Acc(self):
        username = self.lineEdit.text()
        pwd      = self.lineEdit_2.text()
        pwd_2    = self.lineEdit_3.text()
        phone    = self.lineEdit_4.text()
        mail     = self.lineEdit_5.text()
        name     = self.lineEdit_6.text()

        # 提示窗清空 
        self.label_notice1.setText("")
        self.label_notice2.setText("")

        if User().db_connect():
            if username and pwd and pwd_2:
                acc = User(username)
                # 用户已存在
                if acc.PullUser():                              
                    self.label_notice1.setText("ERROR:用户名已经注册！")
                    self.lineEdit.setText("")                   # 清空用户名
                # 密码不一致
                elif pwd != pwd_2:                              # 两次密码不一致
                    self.label_notice1.setText("ERROR:密码不一致，请重新输入密码！")
                    self.lineEdit_2.setText("")
                    self.lineEdit_3.setText("")

                # re.match( "[a-zA-Z0-9_]{8,20}" , "1ad12f23s34455ff66" ) # 密码格式匹配，待后续添加

                # 手机号格式不对（非必填）
                elif phone and (not re.match("[0-9]{11}",phone)):
                    self.label_notice2.setText("手机号格式错误，请输入11位手机号！")
                    self.lineEdit_4.setText("")
                # 邮箱格式不对（非必填）
                elif mail and (not re.match(r'^[0-9a-zA-Z_]+@[a-zA-Z0-9\.]+\.[a-zA-Z]{2,3}$',mail)):
                    self.label_notice2.setText("邮箱格式错误,请输入正确的邮箱！")
                    self.lineEdit_5.setText("")
                else:
                    acc.pwd     = pwd
                    acc.phone   = phone
                    acc.email   = mail
                    acc.name    = name
                    if acc.PushUser():
                        QMessageBox.information(self,
                        '注册完成',
                        '注册完成，点击返回登录界面',
                        QMessageBox.Ok,
                        QMessageBox.Ok)
                        
                        QApplication.processEvents() # 刷新数据
                        self.Quit_Register()
                    else:
                        label_notice1.setText("ERROR:未知错误！")
 
            else:
                self.label_notice1.setText("ERROR:账号密码必须填写！")
        else:
            self.label_notice2.setText("ERROR:请检查数据库链接！") 



#-#-#-#-#-#-#-#-#-#-#-#
def main():
    app = QApplication(sys.argv)
    window = LogIn()
    window.show()
    # app.exec_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
