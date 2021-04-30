from PyQt5              import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets    import *
import sys
from PyQt5.QtCore       import *
from PyQt5.QtGui        import *
import time
from ClassRoomCopy      import *
from AddClassInfo       import *
from DelClassInfo       import *
from CorClassInfo       import *
from ApprClassInfo      import *
from ReturnBack         import *
from logUI              import *
import re

QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)


class AdminUI(QDialog):
    def __init__(self,username):
        super(AdminUI, self).__init__()
        self.username = username
        self.setWindowTitle('教室多媒体钥匙管理系统')
        self.setupUi(self)
        self.retranslateUi(self)
        self.c = ClassRoom().ShowAll()
        self.additem()
        
        # 设置时钟动态显示
        timer = QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start()


    def setupUi(self, Form):
        Form.setObjectName("教室多媒体钥匙管理系统")
        Form.resize(850, 472)
        Form.setFixedSize(855, 472)

        # 背景白色
        palette = QPalette()
        palette.setColor(QPalette.Background, Qt.white)
        self.setPalette(palette)

        iconpath = 'image/login.ico'
        Icon = QIcon(iconpath)
        self.setWindowIcon(Icon)
        # 校徽显示
        pix = QPixmap('image/school.jpg')
        self.lab = QLabel(Form)
        # self.lab.setStyleSheet("border: 2px solid red")
        self.lab.setGeometry(QtCore.QRect(20, 10, 280, 90))
        self.lab.setPixmap(pix)
        self.lab.setScaledContents(True)
        # 头像显示
        pix = QPixmap('image/login.ico')
        self.lab1 = QLabel(Form)
        self.lab1.setStyleSheet("border: 2px solid red")
        self.lab1.setPixmap(pix)
        self.lab1.setScaledContents(True)
        self.lab1.setGeometry(QtCore.QRect(20, 110, 83, 83))
        # 显示标签
        # self.IdLab = QtWidgets.QLabel(Form)
        # self.IdLab.setGeometry(QtCore.QRect(20, 120, 71, 21))
        # self.IdLab.setObjectName("IdLab")
        self.StatusLab = QtWidgets.QLabel(Form)
        self.StatusLab.setGeometry(QtCore.QRect(20, 160, 71, 21))
        self.StatusLab.setObjectName("StatusLab")

        self.TitleLab = QtWidgets.QLabel(Form)
        self.TitleLab.setGeometry(QtCore.QRect(290, 40, 541, 41))
        self.TitleLab.setObjectName("TitleLab")

        # 日志按钮
        self.log_btn = QPushButton(Form)
        self.log_btn.setGeometry(QtCore.QRect(790, 5, 60, 30))
        self.log_btn.setText('管理日志')
        self.log_btn.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.log_btn.clicked.connect(self.show_log)

        # 添加按钮
        self.Add_btn = QPushButton(Form)
        self.Add_btn.setGeometry(QtCore.QRect(760, 110, 80, 30))
        self.Add_btn.setText('添加')
        self.Add_btn.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.Add_btn.clicked.connect(self.AddInfo)

        # 删除按钮
        self.Del_btn = QPushButton(Form)        
        self.Del_btn.setGeometry(QtCore.QRect(760, 150, 80, 30))
        self.Del_btn.setText('删除')
        self.Del_btn.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.Del_btn.clicked.connect(self.DelInfo)

        # 修改按钮
        self.Cor_btn = QPushButton(Form)
        self.Cor_btn.setGeometry(QtCore.QRect(760, 190, 80, 30))
        self.Cor_btn.setText('修改')
        self.Cor_btn.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.Cor_btn.clicked.connect(self.CorInfo)
        
        # 审批按钮
        self.Appr_btn = QPushButton(Form)
        self.Appr_btn.setGeometry(QtCore.QRect(760, 230, 80, 30))
        self.Appr_btn.setText('审批')
        self.Appr_btn.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.Appr_btn.clicked.connect(self.ApprInfo)

        # 归还按钮
        self.return_btn = QPushButton(Form)
        self.return_btn.setGeometry(QtCore.QRect(760,270,80,30))
        self.return_btn.setText('归还钥匙')
        self.return_btn.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.return_btn.clicked.connect(self.ReturnBack)

        #刷新按钮
        self.Refresh_btn = QPushButton(Form)
        self.Refresh_btn.setGeometry(QtCore.QRect(760, 310, 80, 30))
        self.Refresh_btn.setText('刷新')
        self.Refresh_btn.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.Refresh_btn.clicked.connect(self.RefreshInfo)

        #显示数据按钮
        self.display_btn = QPushButton(Form)
        self.display_btn.setGeometry(QtCore.QRect(760, 350, 80, 30))
        self.display_btn.setText('全部数据')
        self.display_btn.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.display_btn.clicked.connect(self.display_data)
        
        # 退出程序按钮
        self.quit_btn = QPushButton(Form)
        self.quit_btn.setGeometry(QtCore.QRect(760,390,80,30))
        self.quit_btn.setText('退出程序')
        self.quit_btn.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.quit_btn.clicked.connect(self.quit_proc)



        # 定义表控件
        self.InfoTable = QtWidgets.QTableWidget(Form)
        self.InfoTable.setSortingEnabled(True)
        self.InfoTable.setGeometry(QtCore.QRect(210, 110, 548, 351))
        self.InfoTable.setObjectName("InfoTable")
        self.InfoTable.setColumnCount(5)
        self.InfoTable.setRowCount(0)
        self.InfoTable.setShowGrid(False)

        # 添加表格
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

        # 边框线
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 180, 185, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(195, 110, 20, 351))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(20, 100, 185, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(10, 110, 20, 351))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(20, 450, 185, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(20, 345, 185, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName('line_6')
        # 时间动态显示
        self.TimeLab = QtWidgets.QLabel(Form)
        self.TimeLab.setGeometry(QtCore.QRect(510, 80, 261, 31))
        self.TimeLab.setObjectName("TimeLab")
        # id 显示
        self.IdEdit = QtWidgets.QLabel(Form)
        self.IdEdit.setGeometry(QtCore.QRect(110, 120, 91, 20))
        self.IdEdit.setObjectName("IdEdit")
        # 状态显示
        self.StatusEdit = QtWidgets.QLabel(Form)
        self.StatusEdit.setGeometry(QtCore.QRect(110, 160, 91, 20))
        self.StatusEdit.setStyleSheet("QLabel{color:rgb(255,0,0);font-size:12px;font-weight:bold}")
        self.StatusEdit.setObjectName("StatusEdit")

        DuringList = ['8:00~9:35',
                      '9:50~11:25',
                      '13:45~15:20',
                      '15:35~17:10',
                      '18:30~21:00',
                      '11:30~12:15',
                      '21:00~21:45',]

        # 左侧查找布局
        # 教学楼选择
        self.BuldingCombo = QComboBox(Form)
        self.BuldingCombo.setGeometry(QtCore.QRect(36, 210, 60, 30))
        self.BuldingCombo.setStyleSheet("QComboBox{background:white}")
        self.BuldingCombo.addItems(['教2','教3','教4'])
        # 楼层选择
        self.FloorCombo = QComboBox(Form)
        self.FloorCombo.setGeometry(QtCore.QRect(141, 210, 60, 30))
        self.FloorCombo.setStyleSheet("QComboBox{background:white}")
        self.FloorCombo.addItems(['1楼','2楼','3楼','4楼'])
        # 时段选择
        self.TimeCombo = QComboBox(Form)
        self.TimeCombo.setGeometry(QtCore.QRect(21, 260, 90, 30))
        self.TimeCombo.setStyleSheet("QComboBox{background:white}")
        self.TimeCombo.addItems(DuringList)
        # 状态选择
        self.StatusCombo = QComboBox(Form)
        self.StatusCombo.setGeometry(QtCore.QRect(141, 260, 60, 30))
        self.StatusCombo.setStyleSheet("QComboBox{background:white}")
        self.StatusCombo.addItems(['可借用','审批中','已借出'])

        # 确认按钮
        self.SearchBtn = QPushButton(Form)
        self.SearchBtn.setText('搜索')
        self.SearchBtn.setGeometry(QtCore.QRect(51, 310, 120, 30))
        self.SearchBtn.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.SearchBtn.clicked.connect(self.confirm_search)

        # 教室搜索输入框
        self.IDEdit = QLineEdit(Form)
        self.IDEdit.setGeometry(QtCore.QRect(51, 370, 120, 30))
        self.IDEdit.setText('如：教2-101')
        # 教室搜索确认按钮
        self.confirm_id = QPushButton(Form)
        self.confirm_id.setGeometry(QtCore.QRect(51, 410, 120, 30))
        self.confirm_id.setText('按照教室搜索')
        self.confirm_id.setStyleSheet('background-color: rgb(255, 255, 255);border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.confirm_id.clicked.connect(self.id_search)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def show_log(self):
        w = logUI()
        w.exec()

    def display_data(self):
        self.additem()

    def show_time(self):
        datatime = QDateTime.currentDateTime()
        localtime = datatime.toString()
        self.TimeLab.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">{localtime}</span></p></body></html>")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        # self.IdLab.setText('ID')
        # self.StatusLab.setText('status')
        self.TitleLab.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">教室多媒体钥匙管理系统管理端</span></p></body></html>"))

        # 添加横向表头
        item = self.InfoTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.InfoTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "教室"))
        item = self.InfoTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "时段"))
        item = self.InfoTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "容纳人数"))
        item = self.InfoTable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "借出状态"))

        self.IdEdit.setText(_translate("Form", f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">{self.username}</span></p><p align=\"center\"><br/></p></body></html>"))
        self.StatusEdit.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Admin</span></p></body></html>"))

        self.InfoTable.setEditTriggers( QAbstractItemView.NoEditTriggers)

    def additem(self):
        # 添加教室信息
        StatusList = ['可借用','审批中','已借出']
        # StatusList = ["<font color = 'green'>可借用</font></html>","<font color = 'yellow'>审批中</font>","<font color = 'red'>已借出</font>"]
        self.c = ClassRoom().ShowAll()
        self.InfoTable.setRowCount(0)
        for i,x in enumerate(self.c):
            self.InfoTable.insertRow(i)
            btn = QPushButton('预定')
            btn.clicked.connect(lambda : self.click_btn(self.InfoTable.currentRow()))

            item = QTableWidgetItem(x['_id'])
            item.setTextAlignment(Qt.AlignCenter)
            self.InfoTable.setItem(i, 0, QTableWidgetItem(item))

            item = QTableWidgetItem(x['name'])
            item.setTextAlignment(Qt.AlignCenter)
            self.InfoTable.setItem(i, 1, QTableWidgetItem(item))

            item = QTableWidgetItem(str(x['seats']))
            item.setTextAlignment(Qt.AlignCenter)
            self.InfoTable.setItem(i, 3, QTableWidgetItem(item))

            item = QTableWidgetItem(x['during'])
            item.setTextAlignment(Qt.AlignCenter)
            self.InfoTable.setItem(i, 2, QTableWidgetItem(item))

            item = QTableWidgetItem(str(StatusList[int(x['status'])]))
            item.setTextAlignment(Qt.AlignCenter)
            # 设置字体颜色
            if int(x['status']) == 0:
                item.setForeground(QBrush(QColor(0,255,0)))
            elif int(x['status']) == 1:
                item.setForeground(QBrush(QColor(255,215,0)))
            elif int(x['status']) == 2:
                item.setForeground(QBrush(QColor(255,0,0)))
            self.InfoTable.setItem(i, 4, QTableWidgetItem(item))

    def AddInfo(self):
        # 添加
        w = AddClassInfo()
        w.exec()

    def DelInfo(self):
        # 删除
        w = DelClassInfo()
        w.exec()

    def CorInfo(self):
        # 修改
        w = CorClassInfo()
        w.exec()

    def ApprInfo(self):
        # 审批
        w = ApprInfo()
        w.exec()
        
    def RefreshInfo(self):
        #刷新 
        # qApp.exit(10086)
        # self.close() 
        self.accept()

    def quit_proc(self):
        self.close()

    def ReturnBack(self):
        w = ReturnBack()
        w.exec()
    
    def id_search(self):
        name = self.IDEdit.text()
        id = 'B'+name[1]+'R'+name[3:]
        id_pat = 'B[2-4]R[0-9]{3}'
        result = re.match(id_pat,id)
        if result:
            # c = ClassRoom(id).PullClassroom()
            # print(c)
            # QMessageBox.information(self, '查询错误', f'教室 {name} 不存在!')
            self.InfoTable.clearContents()
            self.c = ClassRoom().ShowAll()
            # self.InfoTable.setRowCount(0)
            StatusList = ['可借用','审批中','已借出']

            count = 0

            for i,x in enumerate(self.c):
                if x['_id'][:6] == id:
                    item = QTableWidgetItem(x['_id'])
                    item.setTextAlignment(Qt.AlignCenter)
                    self.InfoTable.setItem(count, 0, QTableWidgetItem(item))

                    item = QTableWidgetItem(x['name'])
                    item.setTextAlignment(Qt.AlignCenter)
                    self.InfoTable.setItem(count, 1, QTableWidgetItem(item))

                    item = QTableWidgetItem(str(x['seats']))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.InfoTable.setItem(count, 3, QTableWidgetItem(item))

                    item = QTableWidgetItem(x['during'])
                    item.setTextAlignment(Qt.AlignCenter)
                    self.InfoTable.setItem(count, 2, QTableWidgetItem(item))

                    item = QTableWidgetItem(str(StatusList[int(x['status'])]))

                    if int(x['status']) == 0:
                        item.setForeground(QBrush(QColor(0,255,0)))
                    elif int(x['status']) == 1:
                        item.setForeground(QBrush(QColor(255,215,0)))
                    elif int(x['status']) == 2:
                        item.setForeground(QBrush(QColor(255,0,0)))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.InfoTable.setItem(count, 4, QTableWidgetItem(item))

                    count += 1
            QMessageBox.information(self, '搜索结果', '查询完毕!')
        else:
            QMessageBox.information(self, '搜索结果', '请按照格式输入教室id')

            

    def confirm_search(self):
        # 清空表格数据
        self.InfoTable.clearContents()
        self.c = ClassRoom().ShowAll()
        # self.InfoTable.setRowCount(0)
        # 获取筛选条件
        buildingNum = self.BuldingCombo.currentText()
        floorNum = self.FloorCombo.currentText()
        timeNum = self.TimeCombo.currentText()
        statusNum = self.StatusCombo.currentText()
        # 加入新的信息
        StatusList = ['可借用','审批中','已借出']
        b = buildingNum[-1]
        f = floorNum[0]
        t = timeNum
        s = StatusList.index(statusNum)
        count = 0
        for i,x in enumerate(self.c):
            # print(b==x['_id'][1])
            # print(f==x['_id'][3])
            # print(t==x['during'])
            if b == str(x['_id'][1]): # and (t == str(x['_id'][3])) and (t == str(x['during'])):
                if f == str(x['_id'][3]):
                    if t == str(x['during']):
                        if s == x['status']:
                            # self.InfoTable.insertRow(count)
                            # btn = QPushButton('预定')
                            # btn.clicked.connect(lambda : self.click_btn(self.InfoTable.currentRow()))

                            item = QTableWidgetItem(x['_id'])
                            item.setTextAlignment(Qt.AlignCenter)
                            self.InfoTable.setItem(count, 0, QTableWidgetItem(item))

                            item = QTableWidgetItem(x['name'])
                            item.setTextAlignment(Qt.AlignCenter)
                            self.InfoTable.setItem(count, 1, QTableWidgetItem(item))

                            item = QTableWidgetItem(str(x['seats']))
                            item.setTextAlignment(Qt.AlignCenter)
                            self.InfoTable.setItem(count, 3, QTableWidgetItem(item))

                            item = QTableWidgetItem(x['during'])
                            item.setTextAlignment(Qt.AlignCenter)
                            self.InfoTable.setItem(count, 2, QTableWidgetItem(item))

                            item = QTableWidgetItem(str(StatusList[int(x['status'])]))
                            item.setTextAlignment(Qt.AlignCenter)

                            if int(x['status']) == 0:
                                item.setForeground(QBrush(QColor(0,255,0)))
                            elif int(x['status']) == 1:
                                item.setForeground(QBrush(QColor(255,215,0)))
                            elif int(x['status']) == 2:
                                item.setForeground(QBrush(QColor(255,0,0)))
                            self.InfoTable.setItem(count, 4, QTableWidgetItem(item))

                            count += 1
        # # else:
        # #     QMessageBox.information(self, '搜索结果', '无查询结果!')
        QMessageBox.information(self, '搜索结果', '查询完毕!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AdminUI('A18011929')
    w.show()
    sys.exit(app.exec_())