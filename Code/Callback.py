from PyQt5.QtWidgets import QApplication, QGridLayout, QMainWindow, QDesktopWidget, QWidget, QPushButton, QLineEdit,QLabel,QDialog,QMessageBox
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Register import *
from LoginMatch import * 
from Student import *
from PyQt5.QtWidgets import *
from User import *


class Callback(QDialog):
    def __init__(self):
        super(Callback,self).__init__()
        self.setWindowTitle('找回密码')
        self.initUI()

    def initUI(self):
        self.resize(300,150)
        iconpath = 'image/login.ico'
        Icon = QIcon(iconpath)
        self.setWindowIcon(Icon)

        # 账号标签
        userLab = QLabel('账号',self)
        userLab.setAlignment(Qt.AlignCenter)
        # 姓名标签
        nameLab = QLabel('姓名',self)
        nameLab.setAlignment(Qt.AlignCenter)
        # 电话标签
        phoneLab = QLabel('电话',self)
        phoneLab.setAlignment(Qt.AlignCenter)
        # 邮箱标签
        mailLab = QLabel('邮箱',self)
        mailLab.setAlignment(Qt.AlignCenter)

        #找回密码显示标签
        self.pwdLab = QLabel('HHHHH')
        self.pwdLab.setAlignment(Qt.AlignCenter)

        # 找回按钮
        btn = QPushButton('找回密码')


        # 账号输入
        self.userEdit = QLineEdit()
        self.userEdit.setAlignment(Qt.AlignCenter)
        # 电话输入
        self.phoneEdit = QLineEdit()
        self.phoneEdit.setAlignment(Qt.AlignCenter)
        # 姓名输入
        self.nameEdit = QLineEdit()
        self.nameEdit.setAlignment(Qt.AlignCenter)
        # 邮箱输入
        self.mailEdit = QLineEdit()
        self.mailEdit.setAlignment(Qt.AlignCenter)

        layout = QGridLayout()
        layout.addWidget(userLab,0,0)
        layout.addWidget(self.userEdit,0,1,1,2)
        layout.addWidget(phoneLab,1,0)
        layout.addWidget(self.phoneEdit, 1,1,1,2)
        layout.addWidget(nameLab, 2,0)
        layout.addWidget(self.nameEdit,2,1,1,2)
        layout.addWidget(mailLab,3,0)
        layout.addWidget(self.mailEdit,3,1,1,2)
        layout.addWidget(self.pwdLab,4,1)
        layout.addWidget(btn,5,1,1,1)
        
        btn.clicked.connect(self.btn_clicked)

        self.setLayout(layout)

    def btn_clicked(self):
        userid = self.userEdit.text()
        phone = self.phoneEdit.text()
        name = self.nameEdit.text()
        mail = self.mailEdit.text()

        UserInstance = User(userid)
        if UserInstance.PullUser():
            if userid == UserInstance.id \
                and phone == UserInstance.phone \
                and name == UserInstance.name \
                and mail == UserInstance.email:
                
                pwd = UserInstance.pwd
                self.pwdLab.setText('密码为：'+pwd)
            else:
                QMessageBox.critical(self, "验证错误", "验证信息有误，请重新输入")
        else:
            QMessageBox.critical(self, "账户错误", "账户不存在，请重新输入")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Callback()
    c.show()
    sys.exit(app.exec_())