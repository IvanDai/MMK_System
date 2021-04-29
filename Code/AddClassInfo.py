from PyQt5.QtWidgets    import *
from PyQt5.QtGui    import *
from PyQt5.QtCore   import *
from Match          import *
from ClassRoomCopy  import *
import sys
import time

class AddClassInfo(QDialog):
    def __init__(self):
        super(AddClassInfo,self).__init__()
        self.setWindowTitle('增加教室数据')
        self.setFixedSize(250, 100)
        self.widget()
        self.setting()
    
    def widget(self):
        self.label_id = QLabel('id')
        self.label_people = QLabel('人数')
        self.edit_id = QLineEdit()
        self.edit_people = QLineEdit()
        self.btn_confirm = QPushButton('确认添加')

        # 绑定命令槽
        self.btn_confirm.clicked.connect(self.click_btn)

    def setting(self):
        layout = QGridLayout()

        self.label_id.setAlignment(Qt.AlignCenter)
        self.label_people.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(self.label_id, 0, 0, 1, 1)
        layout.addWidget(self.label_people, 1, 0, 1, 1)
        layout.addWidget(self.edit_id, 0, 1, 1, 2)
        layout.addWidget(self.edit_people, 1, 1, 1, 2)
        layout.addWidget(self.btn_confirm, 2, 1, 1, 1)
        
        self.setLayout(layout)

    def click_btn(self):
        ID = self.edit_id.text()
        people = self.edit_people.text()
        # 检查是否有该ID存在，如果有，报错
        id_legle = classRoomID_match(ID)
        people_legle = people_match(people)
        mytime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if id_legle and people_legle:
            # 是否有该id存在
            id_exist = ClassRoom(ID,people).PullClassroom()
            if id_exist:
                QMessageBox.critical(self, "添加失败", "该事件已存在，请重新输入或前往修改")
            else:
                result = ClassRoom(ID,people).PushClassroom()
                with open('log.txt','a') as f:
                    f.write(f'{mytime} 管理员 添加了事件 {ID}，座位数 {people}\n')

                QMessageBox.critical(self, "添加成功",f"您已成功添加事件 {ID}")
                
                
        else:
            QMessageBox.critical(self, "添加失败", "您输入的ID或人数不合法，请重新核实")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AddClassInfo()
    w.show()
    sys.exit(app.exec_())