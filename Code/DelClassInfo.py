from PyQt5.QtWidgets    import *
from PyQt5.QtGui    import *
from PyQt5.QtCore   import *
from Match          import *
from ClassRoomCopy  import *
import time
import sys

class DelClassInfo(QDialog):
    def __init__(self):
        super(DelClassInfo,self).__init__()
        self.setWindowTitle('删除教室数据')
        self.setFixedSize(250, 100)
        self.widget()
        self.setting()
    
    def widget(self):
        self.label_id = QLabel('id')
        self.edit_id = QLineEdit()
        self.btn_confirm = QPushButton('确认删除')

        # 绑定事件槽
        self.btn_confirm.clicked.connect(self.click_btn)
    
    def click_btn(self):
        # 判定输入是否合法
        ID = self.edit_id.text()
        id_legle = classRoomID_match(ID)
        mytime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        
        # 判断是否存在
        id_exist = ClassRoom(ID).PullClassroom()
        if not id_exist:
            QMessageBox.critical(self, "失败", "该事件不存在，请输入存在事件")
        else:
            result = ClassRoom(ID).PullClassroom().Delete()
            with open('log.txt','a') as f:
                f.write(f'{mytime} 管理员删除了事件 {ID}\n')
            QMessageBox.critical(self,'删除确认',f'您已删除事件 {ID} ')



    def setting(self):
        layout = QGridLayout()

        self.label_id.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(self.label_id, 0, 0, 1, 1)
        layout.addWidget(self.edit_id, 0, 1, 1, 2)
        layout.addWidget(self.btn_confirm, 2, 1, 1, 1)
        
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = DelClassInfo()
    w.show()
    sys.exit(app.exec_())