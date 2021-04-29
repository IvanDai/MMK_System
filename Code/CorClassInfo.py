from PyQt5.QtWidgets    import *
from PyQt5.QtGui    import *
from PyQt5.QtCore   import *
from Match          import *
from ClassRoomCopy  import *
from User2ClassRoom import *
import sys
import time

class CorClassInfo(QDialog):
    def __init__(self):
        super(CorClassInfo,self).__init__()
        self.setWindowTitle('修改教室数据')
        self.setFixedSize(250, 140)
        self.widget()
        self.setting()
    
    def widget(self):
        self.label_id = QLabel('id')
        self.label_people = QLabel('人数')
        self.label_status = QLabel('状态')
        self.edit_id = QLineEdit()
        self.edit_people = QLineEdit()
        self.edit_status = QLineEdit()
        self.btn_confirm = QPushButton('确认修改')
        self.btn_confirm.clicked.connect(self.click_confirm)

    def setting(self):
        layout = QGridLayout()

        self.label_id.setAlignment(Qt.AlignCenter)
        self.label_people.setAlignment(Qt.AlignCenter)
        self.label_status.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(self.label_id, 0, 0, 1, 1)
        layout.addWidget(self.label_people, 1, 0, 1, 1)
        layout.addWidget(self.label_status, 2, 0, 1, 1)


        layout.addWidget(self.edit_id, 0, 1, 1, 2)
        layout.addWidget(self.edit_people, 1, 1, 1, 2)
        layout.addWidget(self.edit_status, 2, 1, 1, 2)
        layout.addWidget(self.btn_confirm, 3, 1, 1, 1)
        
        self.setLayout(layout)
    
    def click_confirm(self):
        ID = self.edit_id.text()
        people = self.edit_people.text()
        status = self.edit_status.text()
        # 判断是否合法
        id_legle = classRoomID_match(ID)
        people_legle = people_match(people)
        status_legle = 1 if int(status) in [0,1,2,3,4,5,] else 0
        mytime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 判断是否存在
        if id_legle and people_legle and status_legle:
            id_exist = ClassRoom(ID).PullClassroom()
            if not id_exist:
                QMessageBox.critical(self,'错误',f'事件 {ID} 不存在，请重新输入')
            else:
                ClassRoom(ID,people,status = int(status)).PushClassroom()
                if status:
                    User2ClassRoom(ID,'Administer',status).PushUC()
                    with open('log.txt','a') as f:
                        f.write(f'{mytime} 管理员修改了事件 {ID} 座位 {people} 状态 {status}\n')
                QMessageBox.critical(self,'成功',f'您已修改事件 {ID}')
        else:
            QMessageBox.critical(self,'错误',f'格式错误，请重新输入')


        # 执行修改操作


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CorClassInfo()
    w.show()
    sys.exit(app.exec_())