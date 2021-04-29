from PyQt5.QtWidgets    import *
import sys
from PyQt5.QtGui        import *
from PyQt5.QtCore       import *
from Register           import *
from Match              import * 
from Student            import *
from Callback           import *
from Admin              import *

class LoginUI(QWidget):
    def __init__(self):
        super(LoginUI,self).__init__()

        # 界面图标
        # icon = QIcon()
        # icon.addPixmap(QPixmap('image\login.ico'))

        # 应用界面
        # 设置登录状态选项
        self.admin_status = 0
        self.user_status = 0
        self.initUI()
        self.username = '' 

    def initUI(self):
        # 窗口大小
        self.resize(400,200)
        self.setFixedSize(280, 110)

        # 窗口标题
        self.setWindowTitle('系统登陆')

        # 窗口半透明
        self.setWindowOpacity(0.8) # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明

        # TODO: 背景图
        # self.setAutoFillBackground(True) #一定要加上
        # palette=QPalette()
        # palette.setBrush(QPalette.Background, QBrush(QPixmap('./image/LoginBackground.jpg')))
        # self.setPalette(palette)
        self.setStyleSheet('background') 
        # 字体
        font = QtGui.QFont() 
        font.setFamily('微软雅黑')
        font.setBold(True) 
        
        # 隐藏边框
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框


        # 窗口图标 
        iconpath = 'image/login.ico'
        Icon = QIcon(iconpath)
        self.setWindowIcon(Icon)

        # 账号密码输入标签
        userLab = QLabel('账号:')
        userLab.setAlignment(Qt.AlignCenter)
        userLab.setStyleSheet('color:white')
        userLab.setFont(font)

        passwardLab = QLabel('密码:')
        passwardLab.setAlignment(Qt.AlignCenter)
        passwardLab.setStyleSheet('color:white')
        passwardLab.setFont(font)

        self.userEdit = QLineEdit()
        self.passwardEdit = QLineEdit()
        self.passwardEdit.setEchoMode(QLineEdit.Password)
        
        # 登录
        LoginBtn = QPushButton("登录",self)

        # 注册
        RegistBtn = QPushButton("注册",self)

        # 找回
        CallbackBtn = QPushButton("找回密码",self)

        # TODO:注销

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
                    self.username = username
                    if username[0] == 'B':
                        # 如果以B开头则进入普通用户界面
                        self.setVisible(False)
                        self.Student = Ui_Form(username)
                        a = self.Student.exec()
                        if a:
                            self.Login_Pushed()
                    else:
                        # 如果以A开头则进入管理员界面
                        self.setVisible(False)
                        self.AdminUI = AdminUI(username)
                        a = self.AdminUI.exec_()
                        if a:
                            self.Login_Pushed() 
  
                else:
                    QMessageBox.information(self, '密码错误', '密码错误，请重新输入') 
            else:
                # 如果登陆失败，弹窗提示
                QMessageBox.critical(self, "输入错误", "账号或密码格式错误，请重新输入")

    def Register_Pushed(self):
        self.setVisible(False)
        ui = Regist()
        ui.exec()
        self.setVisible(True)

    def Callback_Pushed(self):
        self.setVisible(False)
        ui = Callback()
        ui.exec()
        self.setVisible(True)


if __name__ == '__main__':
    UI =  QApplication(sys.argv)
    w = LoginUI()
    w.show()
    UI.exec_()

    # with open('cache.txt','r') as f:
        # line = f.readline()
        
    # username = line[:9]
    # user_status = int(line[9])
    # admin_status = int(line[-1])

    # # 开启登录窗口
    # if user_status is 1 and admin_status is 0:
        # # 用户端
        # UIS = QApplication(sys.argv)
        # studentWin = Ui_Form(username)
        # studentWin.show()
        # UIS.exec_()
    # elif user_status is 0 and admin_status is 1:
        # # 管理端
        # UIA = QApplication(sys.argv)
        # adminWin = AdminUI(username)
        # adminWin.show()
        # UIA.exec_()
