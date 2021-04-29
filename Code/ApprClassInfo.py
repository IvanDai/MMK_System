from PyQt5.QtWidgets    import *
from PyQt5.QtGui    import *
from PyQt5.QtCore   import *
from ClassRoomCopy  import *
import sys
from User2ClassRoom import *
import time

class ApprInfo(QDialog):
    def __init__(self):
        super(ApprInfo,self).__init__()
        self.setFixedSize(350,300)
        self.setWindowTitle('审批')
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
            if l.status == 1:
                line = x['user_id'].ljust(14,' ') + l.id.ljust(12,' ') + l.name.ljust(12,' ') + l.during
                item = QListWidgetItem(line)
                # item.setTextAlignment(Qt.AlignCenter)
                self.Appr_list.addItem(item)

    def appr(self):
        info = self.Appr_list.currentItem().text()
        _id = info[14:21]
        c = ClassRoom(_id).PullClassroom()
        ClassRoom(_id,c.seats,status=2).PushClassroom()
        User2ClassRoom(_id,status=2).PushUC()
        # 获取数据细节
        l = User2ClassRoom(_id).PullUC()

        curItem = self.Appr_list.currentRow()
        self.Appr_list.takeItem(curItem)
        mytime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open('log.txt','a') as f:
            f.write(f'{mytime} 管理员审批通过了 {l.user_id} 申请的事件 {l._id}\n')
        QMessageBox.information(self, '审批结果', f'已同意 用户 {l.user_id} 对事件 {l._id} 的申请!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ApprInfo()
    w.exec()