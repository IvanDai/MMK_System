from PyQt5              import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets    import *
import sys
from PyQt5.QtCore       import *
from PyQt5.QtGui        import *
import time
from ClassRoom          import *

QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

class Admin(QWidget):
    def __init__(self,username):
        super(Admin, self).__init__()
        self.username = username
        self.setWindowTitle('教室多媒体钥匙管理系统')
        self.setupUi(self)
        self.retranslateUi(self)
        self.additem()
        
        # 设置时钟动态显示
        timer = QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start()


    def setupUi(self, Form):
        Form.setObjectName("教室多媒体钥匙管理系统")
        Form.resize(850, 472)
        Form.setFixedSize(850, 472)


        iconpath = 'image/login.ico'
        Icon = QIcon(iconpath)
        self.setWindowIcon(Icon)

        self.IdLab = QtWidgets.QLabel(Form)
        self.IdLab.setGeometry(QtCore.QRect(20, 120, 71, 21))
        self.IdLab.setObjectName("IdLab")
        self.StatusLab = QtWidgets.QLabel(Form)
        self.StatusLab.setGeometry(QtCore.QRect(20, 160, 71, 21))
        self.StatusLab.setObjectName("StatusLab")
        self.TitleLab = QtWidgets.QLabel(Form)
        self.TitleLab.setGeometry(QtCore.QRect(150, 20, 541, 41))
        self.TitleLab.setObjectName("TitleLab")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 180, 291, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.ClassroomLab = QtWidgets.QLabel(Form)
        self.ClassroomLab.setGeometry(QtCore.QRect(90, 180, 111, 61))
        self.ClassroomLab.setObjectName("ClassroomLab")
        self.ClassList = QtWidgets.QListWidget(Form)
        self.ClassList.setGeometry(QtCore.QRect(70, 220, 171, 85))
        self.ClassList.setObjectName("ClassList")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ClassList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ClassList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ClassList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.ClassList.addItem(item)
        self.TimeclssifyLab = QtWidgets.QLabel(Form)
        self.TimeclssifyLab.setGeometry(QtCore.QRect(90, 300, 101, 51))
        self.TimeclssifyLab.setObjectName("TimeclssifyLab")
        self.TimeList = QtWidgets.QListWidget(Form)
        self.TimeList.setGeometry(QtCore.QRect(70, 340, 171, 101))
        self.TimeList.setObjectName("TimeList")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TimeList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TimeList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TimeList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TimeList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TimeList.addItem(item)

        self.Add_btn = QPushButton(Form)
        self.Add_btn.setGeometry(QtCore.QRect(760, 110, 80, 30))
        self.Add_btn.setText('添加')
        self.Add_btn.clicked.connect(self.AddInfo)

        self.Del_btn = QPushButton(Form)        
        self.Del_btn.setGeometry(QtCore.QRect(760, 150, 80, 30))
        self.Del_btn.setText('删除')
        self.Del_btn.clicked.connect(self.DelInfo)

        self.Cor_btn = QPushButton(Form)
        self.Cor_btn.setGeometry(QtCore.QRect(760, 190, 80, 30))
        self.Cor_btn.setText('修改')
        self.Cor_btn.clicked.connect(self.CorInfo)
        
        self.Find_btn = QPushButton(Form)
        self.Find_btn.setGeometry(QtCore.QRect(760, 230, 80, 30))
        self.Find_btn.setText('查找')
        self.Find_btn.clicked.connect(self.FindInfo)

        self.Appr_btn = QPushButton(Form)
        self.Appr_btn.setGeometry(QtCore.QRect(760, 270, 80, 30))
        self.Appr_btn.setText('审批')
        self.Appr_btn.clicked.connect(self.ApprInfo)

        self.InfoTable = QtWidgets.QTableWidget(Form)
        self.InfoTable.setSortingEnabled(True)
        self.InfoTable.setGeometry(QtCore.QRect(320, 110, 418, 351))
        # self.InfoTable.setGeometry(QtCore.QRect(500,110,500,480))
        self.InfoTable.setObjectName("InfoTable")
        self.InfoTable.setColumnCount(4)
        self.InfoTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.InfoTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.InfoTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.InfoTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.InfoTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.InfoTable.setHorizontalHeaderItem(4, item)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(300, 110, 20, 351))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(17, 100, 291, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(10, 110, 20, 351))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(20, 450, 291, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.TimeLab = QtWidgets.QLabel(Form)
        self.TimeLab.setGeometry(QtCore.QRect(310, 70, 251, 31))
        self.TimeLab.setObjectName("TimeLab")
        self.IdEdit = QtWidgets.QLabel(Form)
        self.IdEdit.setGeometry(QtCore.QRect(110, 120, 91, 20))
        self.IdEdit.setObjectName("IdEdit")
        self.StatusEdit = QtWidgets.QLabel(Form)
        self.StatusEdit.setGeometry(QtCore.QRect(110, 160, 91, 20))
        self.StatusEdit.setObjectName("StatusEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def show_time(self):
        datatime = QDateTime.currentDateTime()
        localtime = datatime.toString()
        self.TimeLab.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">{localtime}</span></p></body></html>")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.IdLab.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">ID</span></p></body></html>"))
        self.StatusLab.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">借用状态</span></p></body></html>"))
        self.TitleLab.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">教室多媒体钥匙管理系统管理端</span></p></body></html>"))
        self.ClassroomLab.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">按教室分类</span></p></body></html>"))
        __sortingEnabled = self.ClassList.isSortingEnabled()
        self.ClassList.setSortingEnabled(False)
        item = self.ClassList.item(0)
        item.setText(_translate("Form", "教一"))
        item = self.ClassList.item(1)
        item.setText(_translate("Form", "教二"))
        item = self.ClassList.item(2)
        item.setText(_translate("Form", "教三"))
        item = self.ClassList.item(3)
        item.setText(_translate("Form", "教四"))
        self.ClassList.setSortingEnabled(__sortingEnabled)
        self.TimeclssifyLab.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">按时间分类</span></p></body></html>"))
        __sortingEnabled = self.TimeList.isSortingEnabled()
        self.TimeList.setSortingEnabled(False)
        item = self.TimeList.item(0)
        item.setText(_translate("Form", "周一"))
        item = self.TimeList.item(1)
        item.setText(_translate("Form", "周二"))
        item = self.TimeList.item(2)
        item.setText(_translate("Form", "周三"))
        item = self.TimeList.item(3)
        item.setText(_translate("Form", "周四"))
        item = self.TimeList.item(4)
        item.setText(_translate("Form", "周五"))
        self.TimeList.setSortingEnabled(__sortingEnabled)
        item = self.InfoTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.InfoTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "教室"))
        item = self.InfoTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "可容纳人数"))
        item = self.InfoTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "教室状态"))
        # item = self.InfoTable.horizontalHeaderItem(4)
        # item.setText(_translate("Form", "操作信息"))

        # self.TimeLab.setText(_translate("Form", f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">{localtime}</span></p></body></html>"))
        self.IdEdit.setText(_translate("Form", f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">{self.username}</span></p><p align=\"center\"><br/></p></body></html>"))
        self.StatusEdit.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Admin</span></p></body></html>"))

    def additem(self):
        # 添加教室信息
        c = ClassRoom().ShowAll()
        for i,x in enumerate(c):
            self.InfoTable.insertRow(i)

            item = QTableWidgetItem(x['_id'])
            item.setTextAlignment(Qt.AlignCenter)
            self.InfoTable.setItem(i, 0, QTableWidgetItem(item))

            item = QTableWidgetItem(x['name'])
            item.setTextAlignment(Qt.AlignCenter)
            self.InfoTable.setItem(i, 1, QTableWidgetItem(item))

            item = QTableWidgetItem(str(x['seats']))
            item.setTextAlignment(Qt.AlignCenter)
            self.InfoTable.setItem(i, 2, QTableWidgetItem(item))

        # 设置不可更改
        self.InfoTable.setEditTriggers( QAbstractItemView.NoEditTriggers)

    def AddInfo(self):
        # 添加
        print(1)
    
    def DelInfo(self):
        # 删除
        print(2)

    def CorInfo(self):
        # 修改
        print(3)

    def FindInfo(self):
        # 查询
        print(4)

    def ApprInfo(self):
        # 审批
        print(5)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Admin('hha')
    w.show()
    app.exit(app.exec_())