import sys,os
import re
import time
import datetime
from PyQt5.uic import loadUiType
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from db_User import *
from db_ClassRoom import *
from db_Event import *

from Login import *
from SetTheme import *


userapp,_   = loadUiType('../ui/MMKSystem.ui')

class UserApp(QMainWindow,userapp):
    quan_dict = {
        0:"",
        1:"第1-2节课",
        2:"第3-5节课",
        3:"第6-7节课",
        4:"第8-9节课",}
    status_dict = {
        0:"待审核",
        1:"已通过",
        2:"已过期"}

    def __init__(self,acc):
        self.acc = acc
        QWidget.__init__(self)
        self.setupUi(self)
        # 设置主题
        from SetTheme import Theme
        Theme(self)
        # 更新数据库
        Event().Update()
        self.Handle_Buttons()

    def Handle_Buttons(self):
        ###########################  Tab切换  ###############################
        self.tabWidget.currentChanged.connect(self.Tab_Change)

        ############################  Tab1  ################################
        # 时间选择相关
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit.setMinimumDate(QDate.currentDate())
        print(QDateTime.currentDateTime())
        # 表格初始化
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # 填满
        self.tableWidget.setAlternatingRowColors(True) # 隔行变色

        # 查询键链接
        self.pushButton_2.clicked.connect(self.Check_Room)

        # 表格双击事件
        self.tableWidget.clicked.connect(self.Add_Lent)
        # 借用事件
        self.pushButton_6.clicked.connect(self.Lend_Classroom)
        ############################  Tab2  ################################
        # 表格初始化
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # 填满
        self.tableWidget_2.setAlternatingRowColors(True) # 隔行变色 
        # 链接事件
        self.tableWidget_2.clicked.connect(self.Add_Event)
        self.pushButton_7.clicked.connect(self.Del_Event)

        ############################  左下角  ################################
        # 个人信息修改
        self.pushButton_3.clicked.connect(self.Set_Info)
        self.pushButton_4.clicked.connect(self.Set_Info)
        # 修改主题
        self.pushButton_5.clicked.connect(self.Change_Theme) 
        # 登出
        self.pushButton.clicked.connect(self.Log_Out)

        ############################  左上角  ################################
        self.label.setText(self.acc)
        timer = QTimer(self)
        timer.timeout.connect(self.Show_Time)
        timer.start()

    #---------------------------#  Tab切换  #---------------------------#
    def Tab_Change(self):
        if self.tabWidget.currentIndex()==1:
            self.Load_Self_Event()

    #---------------------------#  Tab1相关  #---------------------------#

    #======查询空教室信息======#
    def Check_Room(self):
        # 重制表格
        for row in range(self.tableWidget.rowCount(),-1,-1):
            self.tableWidget.removeRow(row)

        QApplication.processEvents() # 刷新
        time.sleep(0.5)

        date    = self.dateEdit.date()
        quan    = self.comboBox.currentIndex() + 1
        build   = self.comboBox_2.currentIndex()
        date    = date.toString(Qt.ISODate)
        quant   = self.quan_dict[quan]

        # 查看时间是否合法
        temp_date = str(datetime.date.today())
        temp_quan = self.Check_Quan()
        if date == temp_date and quan <= temp_quan:
            QMessageBox.information(self,"警告",'查询时间已过期，请选择合法时间！',
                                        QMessageBox.Ok,QMessageBox.Ok) 
            return False
        
        rooms = ClassRoom().AllClassroom()
        # 转化为表格
        index = []
        for room in rooms:
            # 查看教学楼是否符合要求
            room_b = int(room['name'][1])
            if build and room_b != build:
                pass
            # 查看是否已经被借用
            elif Event().Check_Event(room['_id'], date, quan):
                pass
            else:
                temp = [room['_id'],room['name'],date,quant,room['seats']]
                index.append(temp)
        items = index
        for i in range(len(items)):
            item_row = items[i]
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for j in range(len(item_row)):
                item = QTableWidgetItem(str(items[i][j]))
                self.tableWidget.setItem(row,j,item)

        print(date,quan,build)
        return True
    
    #======   借用相关  ======#
    def Add_Lent(self,index):
        row = index.row()
        roomID   = self.tableWidget.item(row, 0).text()
        roomName = self.tableWidget.item(row, 1).text()
        date     = self.tableWidget.item(row, 2).text()
        quan     = self.tableWidget.item(row, 3).text() # 文字版时间段
        
        self.label_12.setText(roomID)
        self.label_13.setText(roomName)
        self.label_14.setText(date)
        self.label_15.setText(quan)

    def Lend_Classroom(self):
        room_ID     = self.label_12.text()
        room_name   = self.label_13.text()
        date        = self.label_14.text()
        quan        = self.label_15.text()
        reason      = self.lineEdit.text()
        user_ID     = self.acc
        if not reason:
            QMessageBox.information(self,"警告",'请填写申请理由！！',QMessageBox.Ok,QMessageBox.Ok)
        elif room_ID =="无":
            QMessageBox.information(self,"警告",'请选择教室！！',
                                    QMessageBox.Ok,QMessageBox.Ok) 
        else:
            quan = list(self.quan_dict.values()).index(quan) # 反向查找字典
            if Event().Add_Event(date, quan, room_ID, user_ID, reason):
                QMessageBox.information(self,'登记完成','登记完成，请耐心等待管理员审批！',
                                        QMessageBox.Ok,QMessageBox.Ok)
                self.Check_Room()
            else:
                QMessageBox.information(self,"警告",'教室已被借用，请重新选择教室！',
                                        QMessageBox.Ok,QMessageBox.Ok)

    #---------------------------#  Tab2相关  #---------------------------#

    #======查询个人记录======#
    def Load_Self_Event(self):

        # 清空窗体内容
        for row in range(self.tableWidget_2.rowCount(),-1,-1):
            self.tableWidget_2.removeRow(row)
        QApplication.processEvents() # 刷新
        # 填充相关
        events = Event().Check_Event_User(self.acc)
        index = []
        for event in events:
            # 基本信息处理
            room_id = event['RoomID']                     # ID
            name = "教" + room_id[1] + "-" + room_id[3:6] # Name
            quan = self.quan_dict[int(event['quantuma'])]      # 时间段
            status = self.status_dict[int(event['status'])]
            # 整合信息
            temp = [event['_id'],name,event['date'],quan,status]
            index.append(temp)
        items = index
        for i in range(len(items)):
            item_row = items[i]
            row = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row)
            for j in range(len(item_row)):
                item = QTableWidgetItem(str(items[i][j]))
                self.tableWidget_2.setItem(row,j,item)
                if item_row[4] == '待审核':
                    self.tableWidget_2.item(row,j).setBackground(QColor(235,200,200))
                if item_row[4] == '已通过':
                    self.tableWidget_2.item(row,j).setBackground(QColor(200,235,200))
                if item_row[4] == '已过期':
                    self.tableWidget_2.item(row,j).setBackground(QColor(200,200,200))
    
    #====== 撤回借用 ======#
    def Add_Event(self,index):
        row = index.row()
        EventID  = self.tableWidget_2.item(row, 0).text()
        roomName = self.tableWidget_2.item(row, 1).text()
        date     = self.tableWidget_2.item(row, 2).text()
        quan     = self.tableWidget_2.item(row, 3).text() # 文字版时间段
        
        self.label_17.setText(EventID)
        self.label_19.setText(roomName)
        self.label_21.setText(date)
        self.label_23.setText(quan)

    def Del_Event(self):
        id = self.label_17.text()
        event = Event()
        if event.Pull_Event(id):
            if event.status == 0:
                A = QMessageBox.question(self,'确认','是否撤销记录？',QMessageBox.Yes | QMessageBox.No)   #创建一个二次确认框
                if A == QMessageBox.Yes:
                    Event().Delete_Event(id)
                    self.Load_Self_Event()
            else:
                QMessageBox.information(self,'警告','已审核或已过期的记录无法撤销！') 
        else:
            QMessageBox.information(self,'警告','未查询到记录')

    #---------------------------#   左上角   #---------------------------#
    def Show_Time(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString()
        self.label_10.setText(text)
        hour = QTime.currentTime().hour()
        if hour < 4 or hour > 18:
            self.label_2.setText("晚上好!")
        elif hour < 10:
            self.label_2.setText("早上好")
        elif hour < 13:
            self.label_2.setText("中午好")
        else:
            self.label_2.setText("下午好") 

    #---------------------------#   左下角   #---------------------------# 
    def Log_Out(self):
        from Login import LogIn
        self.window = LogIn()
        self.close()
        time.sleep(0.5)
        self.window.show()

    def Change_Theme(self):
        from SetTheme import SetThemeWindow
        self.window = SetThemeWindow(self.acc,0)
        self.close()
        self.window.show()
        return

    def Set_Info(self):
        from SetInfo import SetInfoWindow
        self.window = SetInfoWindow(self.acc,0)
        self.close()
        self.window.show()
        return
    
    #---------------------------# 其他功能相关 #---------------------------#
    def Check_Quan(self):
        d = datetime.datetime.now()
        time = d.hour * 100 + d.minute
        if time < 800:
            quant = 0
        elif time < 935:
            quant = 1
        elif time < 1215:
            quant = 2
        elif time < 1520:
            quant = 3
        elif time < 1710:
            quant = 4
        else:
            quant = 10
        return quant


def main():
    app = QApplication(sys.argv)
    window = UserApp("B18012005")
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
