import sys
from PyQt5.QtWidgets import QApplication,\
    QMainWindow,QAction,QLabel,QPushButton,\
    QVBoxLayout,QHBoxLayout,QWidget,QGridLayout


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MMK_System登录窗口')
        self.setFixedSize(300, 400)
        self.grid_layout()

    def grid_layout(self):
        # 两个标签
        usr_label = QLabel('账号')
        pwd_label = QLabel('密码')
        label3    = QLabel('Test')

        # 两个按钮
        button_1 = QPushButton('第一个按钮')
        button_2 = QPushButton('第二个按钮')

        hbox_1 = QHBoxLayout()
        hbox_2 = QHBoxLayout()

        # 在水平盒子1中添加一个标签和一个按钮
        hbox_1.addWidget(usr_label)
        hbox_1.addWidget(pwd_label)
        hbox_1.addWidget(label3)

        # 在水平盒子2中添加标签2和按钮2
        hbox_2.addWidget(button_1)
        hbox_2.addWidget(button_2)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)


        # 创建一个窗口部件，设置布局为垂直盒子
        layout_widget = QWidget()
        layout_widget.setLayout(vbox)
        # layout_widget.setFixedSize(300, 150)

        self.setCentralWidget(layout_widget)


        # 创建一个网格布局对象
        # grid_layout = QGridLayout()

        # # 在网格中添加窗口部件
        # grid_layout.addWidget(usr_label, 0, 0)  # 放置在0行0列
        # grid_layout.addWidget(button_1, 0, 1)  # 0行1列
        # grid_layout.addWidget(pwd_label, 1, 0)  # 1行0列
        # grid_layout.addWidget(button_2, 1, 1)  # 1行1列

        # # 创建一个窗口对象
        # layout_widget = QWidget()
        # # 设置窗口的布局层
        # layout_widget.setLayout(grid_layout)
        #
        # self.setCentralWidget(layout_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = LoginWindow()
    gui.show()
    sys.exit(app.exec_())