import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from random import randint

class Game(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(500, 500, 600, 480)
        self.setWindowTitle('捡石头')

        self.bt1 = QPushButton('start', self)
        self.bt1.setGeometry(200, 45, 200 ,100)
        self.bt1.setToolTip('<b>聪明语制作</b>')

        self.bt2 = QPushButton('rules', self)
        self.bt2.setGeometry(200, 190, 200 ,100)
        self.bt2.setToolTip('<b>聪明语制作</b>')
        self.bt2.clicked.connect(self.showMessage) 

        self.bt3 = QPushButton('about', self)
        self.bt3.setGeometry(200, 335, 200 ,100)
        self.bt3.setToolTip('<b>聪明语制作</b>')
        self.bt3.clicked.connect(self.showMessage)  

        self.show()    
        
    def closeEvent(self, event):

        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()        
        else:
            event.ignore()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Game()
    sys.exit(app.exec_())