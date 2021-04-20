from PyQt5.QtWidgets import QApplication, QVBoxLayout, QMainWindow, QDesktopWidget, QWidget, QPushButton, QHBoxLayout, QToolTip, QDialog,QLabel
import sys
from PyQt5.QtGui import QFont, QPalette, QPixmap
from PyQt5.QtCore import Qt
class MyWindow(QWidget):
	def __init__(self):
		super(MyWindow,self).__init__()
		self.initUI()

	def initUI(self):
		self.resize(1000,800)
		self.setWindowTitle('LabelTest')

		lab1 = QLabel(self)
		lab2 = QLabel(self)
		lab3 = QLabel(self)
		lab4 = QLabel(self)

		lab1.setText('<font color = green size = 12>Welcome Here</font>')
		lab1.setAutoFillBackground(True)
		palette = QPalette()
		palette.setColor(QPalette.Window, Qt.blue)
		lab1.setPalette(palette)
		lab1.setAlignment(Qt.AlignCenter)

		lab2.setText('<font color = blue size = 5>Following is a picture.')
		
		lab3.setAlignment(Qt.AlignCenter)
		lab3.setPixmap(QPixmap('./image/desktop.jpg'))

		lab4.setText('<font color = blue size = 6>Redemption')
		lab4.setAlignment(Qt.AlignRight)
		

		vbox = QVBoxLayout()
		vbox.addWidget(lab1)
		vbox.addWidget(lab2)
		vbox.addWidget(lab3)
		vbox.addWidget(lab4)

		lab2.linkHovered.connect(self.linkHovered_lab2)
		lab4.linkActivated.connect(self.linkActivate_lab4)
		self.setLayout(vbox)

	def linkHovered_lab2(self):
		print('Covering lab2')

	def linkActivate_lab4(self):
		print('Activating lab4')

if __name__ == '__main__':


	app = QApplication(sys.argv)
	w = MyWindow()
	w.show()
	app.exec_()

