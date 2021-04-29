from PyQt5.QtWidgets    import *
from PyQt5.QtGui    import *
from PyQt5.QtCore   import *
from ClassRoomCopy  import *
import sys
from User2ClassRoom import *
import time

class ReturnBack(QDialog):
    def __init__(self):
        super(ReturnBack,self).__init__()
        self.setFixedSize(350,300)
        self.setWindowTitle('归还')
        self.initUI()
        self.addItem()

    def initUI(self):
        layout = QFormLayout()
        self.Appr_list = QListWidget()
        self.Appr_list.itemDoubleClicked.connect(self.appr)
        layout.addWidget(self.Appr_list)
        self.setLayout(layout)

    def addItem(self):
        self.u = User2ClassRoom().ShowAll()
        title = '借用者'.center(14,' ')+'事件'.center(14,' ')+'教室'.center(13,' ')+'时段'.center(18,' ')
        item = QListWidgetItem(title)
        self.Appr_list.addItem(item)
        for x in self.u:
            l = ClassRoom(x['_id']).PullClassroom()
            if l.status == 2:
                line = x['user_id'].ljust(14,' ') + l.id.ljust(12,' ') + l.name.ljust(12,' ') + l.during
                item = QListWidgetItem(line)
                # item.setTextAlignment(Qt.AlignCenter)
                self.Appr_list.addItem(item)

    def appr(self):
        info = self.Appr_list.currentItem().text()
        _id = info[14:21]
        c = ClassRoom(_id).PullClassroom()
        ClassRoom(_id,c.seats,status=0).PushClassroom()
        # 获取数据细节
        l = User2ClassRoom(_id).PullUC()

        mytime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open('log.txt','a') as f:
            f.write(f'{mytime} 管理员归还了 用户 {l.user_id} 的事件 {l._id}\n')

        User2ClassRoom(_id).Delete()
        curItem = self.Appr_list.currentRow()
        self.Appr_list.takeItem(curItem)

        
        QMessageBox.information(self, '归还结果', '已经成功归还!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ApprInfo()
    w.exec()