import sys,os
import re
from PyQt5.uic import loadUiType
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json


settheme,_ = loadUiType('../ui/SetTheme.ui')
JSON_PATH  = '../config/config.json'

class SetThemeWindow(QDialog,settheme):
    def __init__(self,usr_id,admin):
        QWidget.__init__(self)

        self.usr_id = usr_id
        self.admin  = admin
        self.setupUi(self)
        self.t = Theme(self)   # 创建主题，t.theme["Theme"]用于存储主题
        self.t_backup = self.t.theme["Theme"]
        self.Handle_Buttons()
    
    def Handle_Buttons(self):
        self.label_2.setText(Theme.theme_dict[self.t.theme['Theme']])
        self.pushButton.clicked.connect(self.Change_Classic)
        self.pushButton_2.clicked.connect(self.Change_Qdark)
        self.pushButton_6.clicked.connect(self.Change_OD)
        self.pushButton_3.clicked.connect(self.Change_BD)
        self.pushButton_4.clicked.connect(self.Change_GD)
        self.buttonBox.accepted.connect(self.Save_Changes)
        self.buttonBox.rejected.connect(self.Quit)
    
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
        if self.t.theme["Theme"] == self.t_backup:
            self.Quit()
        else:
            A = QMessageBox.question(self,'确认','是否确认保存设置？',QMessageBox.Yes | QMessageBox.No)   #创建一个二次确认框
            if A == QMessageBox.Yes:
                self.t.SaveTheme()
                self.Quit()


    def Change_Classic(self):
        self.t.theme["Theme"] = 0
        self.t.Change_Theme(self)

    def Change_Qdark(self):
        self.t.theme["Theme"] = 1
        self.t.SaveTheme()
        self.t.Change_Theme(self)
    
    def Change_OD(self):
        self.t.theme["Theme"] = 2
        self.t.SaveTheme()
        self.t.Change_Theme(self)
    
    def Change_BD(self):
        self.t.theme["Theme"] = 3
        self.t.SaveTheme()
        self.t.Change_Theme(self)
    
    def Change_GD(self):
        self.t.theme["Theme"] = 4
        self.t.SaveTheme()
        self.t.Change_Theme(self)




class Theme:
    theme_dict = {
        0 : "经典主题",
        1 : "Qdark主题",
        2 : "橙黑主题",
        3 : "蓝黑主题",
        4 : "灰黑主题"}

    def __init__(self,object):
        self.LoadTheme()
        self.Change_Theme(object)

    def LoadTheme(self):
        fp = open(JSON_PATH, "r")
        self.theme = json.load(fp)
    
    def SaveTheme(self):
        json_str = json.dumps(self.theme)
        with open(JSON_PATH, "w+") as json_file:
            json_file.write(json_str)
    
    def Change_Theme(self,object):
        theme = self.theme["Theme"]
        if theme == 1:
            self.Set_Qdark_Theme(object)
        elif theme == 2:
            self.Set_Dark_Orange_Theme(object)
        elif theme == 3:
            self.Set_Dark_Orange_Theme(object)
        elif theme == 4:
            self.Set_Dark_Orange_Theme(object)
        else :
            self.set_Classic_Theme(object)

    def set_Classic_Theme(self,object):
        object.setStyleSheet("")

    def Set_Qdark_Theme(self,object):
        style = open('../themes/qdark.css' , 'r')
        style = style.read()
        object.setStyleSheet(style)

    def Set_Dark_Orange_Theme(self,object): 
        style = open('../themes/darkorange.css' , 'r')
        style = style.read()
        object.setStyleSheet(style)
    
    def Set_Dark_Blue_Theme(self, object): 
        style = open('../themes/darkblue.css' , 'r')
        style = style.read()
        object.setStyleSheet(style)

    def Set_Dark_Gray_Theme(self,object): 
        style = open('../themes/darkgray.css' , 'r')
        style = style.read()
        object.setStyleSheet(style)

def main():
    app = QApplication(sys.argv)
    window = SetThemeWindow('B18012005',0)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
