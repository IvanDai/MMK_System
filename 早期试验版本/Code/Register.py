from PyQt5.QtWidgets import QApplication, QGridLayout, QMainWindow, QDesktopWidget, QWidget, QPushButton, QLineEdit,QLabel,QDialog,QMessageBox
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from  RegisterMatch import *
from User import *

class Regist(QDialog):
    def __init__(self):
        super(Regist,self).__init__()
        self.setWindowTitle('用户注册')
        self.setFixedSize(300,250)
        self.initUI()

    def  initUI(self):
        iconpath = 'image/login.ico'
        Icon = QIcon(iconpath)
        self.setWindowIcon(Icon)

        # 账号标签
        userLab = QLabel('账号',self)
        userLab.setAlignment(Qt.AlignCenter)
        # 密码标签
        passwardLab = QLabel('密码',self)
        passwardLab.setAlignment(Qt.AlignCenter)
        # 确认密码标签
        confirmLab  = QLabel('确认密码',self)
        confirmLab.setAlignment(Qt.AlignCenter)
        # 姓名标签
        nameLab = QLabel('姓名',self)
        nameLab.setAlignment(Qt.AlignCenter)
        # 电话标签
        phoneLab = QLabel('电话',self)
        phoneLab.setAlignment(Qt.AlignCenter)
        # 邮箱标签
        mailLab = QLabel('邮箱',self)
        mailLab.setAlignment(Qt.AlignCenter)

        # 账号输入
        self.userEdit = QLineEdit()
        # 密码输入
        self.passwardEdit = QLineEdit()
        # 设置掩码
        self.passwardEdit.setEchoMode(QLineEdit.Password)
        # 密码确认
        self.confirmEdit = QLineEdit()
        self.confirmEdit.setEchoMode(QLineEdit.Password)
        # 电话输入
        self.phoneEdit = QLineEdit()
        self.phoneEdit.setAlignment(Qt.AlignCenter)
        # 姓名输入
        self.nameEdit = QLineEdit()
        # 邮箱输入
        self.mailEdit = QLineEdit() 
        
        Btn = QPushButton('注册')

        layout = QGridLayout()
        layout.addWidget(userLab,0,0)
        layout.addWidget(self.userEdit,0,1,1,2)
        layout.addWidget(passwardLab,1,0)
        layout.addWidget(self.passwardEdit,1,1,1,2)
        layout.addWidget(confirmLab, 2,0)
        layout.addWidget(self.confirmEdit, 2,1,1,2)
        layout.addWidget(phoneLab,3,0)
        layout.addWidget(self.phoneEdit, 3,1,1,2)
        layout.addWidget(nameLab, 4,0)
        layout.addWidget(self.nameEdit,4,1,1,2)
        layout.addWidget(mailLab,5,0)
        layout.addWidget(self.mailEdit,5,1,1,2)
        layout.addWidget(Btn,6,0,1,3)
        # 链接信号槽 
        Btn.clicked.connect(self.clickBtn)
        
        self.setLayout(layout)

    # 点击注册按钮
    def clickBtn(self):
        print('clicking register btn...')
        user = self.userEdit.text() # 获取id文本
        passward = self.passwardEdit.text() # 获取密码文本
        confirm = self.confirmEdit.text() # 获取确认密码
        name = self.nameEdit.text() # 获取姓名文本
        phone = self.phoneEdit.text() # 获取电话
        mail = self.mailEdit.text() # 获取邮件
        if passward == confirm:
            i_signal = IDmatah(user) # 检查 错误输出False
            p_signal = passwardMatch(passward) # 同上

            if i_signal and p_signal:
            # 接入数据库
                user_exist = User(user).PullUser()
                if not user_exist:
                    User(user,passward,name,phone,mail).PushUser()
                    QMessageBox.information(self, '注册成功', '注册成功，请返回登录') 
                else:
                    QMessageBox.information(self, '用户存在', '注册失败，用户已存在') 
            else:
            # 提示错误，重新输入
                QMessageBox.critical(self, "格式错误", "账号或密码格式错误，请重新输入")
        else:
            QMessageBox.critical(self, "确认错误", "确认密码错误，请重新输入")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    r = Regist()
    r.show()
    sys.exit(app.exec_())