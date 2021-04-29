from PyQt5.QtWidgets import QApplication, QGridLayout, QMainWindow, QDesktopWidget, QWidget, QPushButton, QLineEdit,QLabel,QDialog,QMessageBox
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Register import *
from LoginMatch import * 
from Student import *
from Callback import *

class LoginUI(QWidget):
    def __init__(self):
        super(LoginUI,self).__init__()

        # 界面图标
        # icon = QIcon()
        # icon.addPixmap(QPixmap('image\login.ico'))

        # 应用界面
        self.initUI()
        

    def initUI(self):
        # 窗口大小
        self.resize(400,200)
        self.setFixedSize(300, 150)

        # 窗口标题
        self.setWindowTitle('系统登陆')

        # 窗口图标 
        iconpath = 'image/login.ico'
        Icon = QIcon(iconpath)
        self.setWindowIcon(Icon)

        # 账号密码输入标签
        userLab = QLabel('账号')
        userLab.setAlignment(Qt.AlignCenter)
        passwardLab = QLabel('密码')
        passwardLab.setAlignment(Qt.AlignCenter)
        self.userEdit = QLineEdit()
        self.passwardEdit = QLineEdit()
        self.passwardEdit.setEchoMode(QLineEdit.Password)
        
        # 登录
        LoginBtn = QPushButton("登录",self)

        # 注册
        RegistBtn = QPushButton("注册",self)

        # 找回
        CallbackBtn = QPushButton("找回密码",self)

        # 注销

        layout = QGridLayout()
        layout.addWidget(userLab,0,0)
        layout.addWidget(self.userEdit,0,1,1,2)
        layout.addWidget(passwardLab,1,0)
        layout.addWidget(self.passwardEdit, 1, 1, 1, 2)

        layout.addWidget(LoginBtn, 2, 0)
        layout.addWidget(RegistBtn, 2, 1)
        layout.addWidget(CallbackBtn, 2, 2)

        # 链接控件槽
        # LoginBtn.clicked.connect(self.show_manu)
        LoginBtn.clicked.connect(self.Login_Pushed)
        RegistBtn.clicked.connect(self.Register_Pushed)
        CallbackBtn.clicked.connect(self.Callback_Pushed)
        self.setLayout(layout)

    def Login_Pushed(self):
        username = self.userEdit.text()
        password = self.passwardEdit.text()

        # 检验操作
        check_user = CheckName(username)
        check_password = CheckPassword(password)

        user = User(username).PullUser()
        
        if not user:
            QMessageBox.critical(self, "用户错误", "用户不存在，请前往注册")
        else:

            if check_user and check_password:
                # 如果成功登录 则打开主信息界面
                user = User(username).PullUser()
                userPassword = User(username).pwd
                if password == userPassword and user:
                    self.Student = Ui_Form(username)
                    self.Student.show()
                    self.close()
                else:
                    QMessageBox.information(self, '密码错误', '密码错误，请重新输入') 
            else:
                # 如果登陆失败，弹窗提示
                QMessageBox.critical(self, "输入错误", "账号或密码错误，请重新输入")

    def Register_Pushed(self):
        self.setVisible(False)
        ui = Regist()
        ui.exec()
        self.setVisible(True)

    def Callback_Pushed(self):
        print('Calling back...')
        self.setVisible(False)
        ui = Callback()
        ui.exec()
        self.setVisible(True)

    def show_manu(self):
        mainUI = Manu()
        mainUI.show()
        


if __name__ == '__main__':
    UI =  QApplication(sys.argv)
    w = LoginUI()
    w.show()
    sys.exit(UI.exec())


        
