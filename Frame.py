import os
import sys
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication)
from PyQt5.QtCore import (Qt, pyqtSignal)
from PyQt5.QtGui import (QPainter, QPen, QBrush)
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QGridLayout, QLineEdit, QRadioButton, QPushButton, QSlider, QVBoxLayout, QApplication, QWidget, QPushButton, QMessageBox, QLabel)
from PyQt5.QtWidgets import (QDialog, QSpinBox, QComboBox, QDialogButtonBox, QFormLayout, QVBoxLayout, QHBoxLayout)
from Ui_stone import Ui_Form
from Ui_stone2 import Ui_Form1

class Ui_Frame1(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("stone_game_menu")
        self.resize(640, 480)

        btn_start = QPushButton('start')
        btn_start.setMaximumSize(100000, 100000)

        btn_rules = QPushButton('rules')
        btn_rules.setMaximumSize(100000, 100000)
        btn_rules.setToolTip('<b>快点击我看规则</b>')

        btn_about = QPushButton('about')
        btn_about.setMaximumSize(100000, 100000)
        btn_about.setToolTip('<b>咸鱼制作</b>')

        layout = QVBoxLayout(self)
        layout.addWidget(btn_start)
        layout.addWidget(btn_rules)
        layout.addWidget(btn_about)
        self.setLayout(layout)

        btn_start.clicked.connect(self.OnClick_Start)
        btn_rules.clicked.connect(self.OnClick_Rules)
        btn_about.clicked.connect(self.OnClick_About)

    def OnClick_About(self):
        QMessageBox.about(self, '关于', 'https://github.com/dcyril233/CatchStoneGame')

    def OnClick_Rules(self):
        QMessageBox.about(self, 'rules', '玩家需要设置先手或后手，与电脑依次选择某一石子堆并拾取任意数量的石子，拾走最后一个石子的一方获胜')

    def OnClick_Start(self):
        self.hide()
        self.next.show()

class Ui_Frame2(QWidget):
    signal = pyqtSignal(list)

    def __init__(self):
        QWidget.__init__(self)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #设置只能输入int类型的数据
        self.ui.Btn_input1.setValidator(QtGui.QIntValidator(1, 1000))
        self.ui.Btn_input2.setValidator(QtGui.QIntValidator(1, 1000))
        self.ui.Btn_input3.setValidator(QtGui.QIntValidator(1, 1000))

        self.ui.Btn_OK.clicked.connect(self.OnClick_OK)
        self.ui.Btn_secondhand.clicked.connect(self.first_second)
        self.ui.Btn_firsthand.clicked.connect(self.first_second)

    def first_second(self):
        if self.ui.Btn_firsthand.isChecked()==True:
            self.order = 1
        else:
            self.order = 0

    def OnClick_OK(self):
        try:
            num1 = int(self.ui.Btn_input1.text())
            num2 = int(self.ui.Btn_input2.text())
            num3 = int(self.ui.Btn_input3.text())
            string = [num1, num2, num3, self.order]
            self.signal.emit(string)
            self.hide()
            self.next.show()            
        except:
            QMessageBox.warning(self, 'warning', '请输入石头数量')

class Ui_Frame3(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.num_temp=[]
        self.Last_Num=[]
        self.f_s = 1

        self.ui = Ui_Form1()
        self.ui.setupUi(self)

        self.ui.Btn_input1.setValidator(QtGui.QIntValidator(1, 1000))
        self.ui.Btn_input2.setValidator(QtGui.QIntValidator(1, 1000))
        self.ui.Btn_input3.setValidator(QtGui.QIntValidator(1, 1000))

        self.ui.Btn_OK.clicked.connect(self.OnClick_OK)

        self.ui.Btn_input1.textEdited[str].connect(lambda :self.auto_input1())
        self.ui.Btn_input2.textEdited[str].connect(lambda :self.auto_input2())
        self.ui.Btn_input3.textEdited[str].connect(lambda :self.auto_input3())

        if self.f_s == 0:
            num = self.machine(self.num_temp)
            self.ui.Btn_num1.setText(str(num[0]))
            self.ui.Btn_num2.setText(str(num[1]))
            self.ui.Btn_num3.setText(str(num[2]))
            self.Last_Num = num[:]

    def auto_input1(self):
        self.ui.Btn_input2.setText(str(self.Last_Num[1]))
        self.ui.Btn_input3.setText(str(self.Last_Num[2]))

    def auto_input2(self):
        self.ui.Btn_input1.setText(str(self.Last_Num[0]))
        self.ui.Btn_input3.setText(str(self.Last_Num[2]))        

    def auto_input3(self):
        self.ui.Btn_input1.setText(str(self.Last_Num[0]))
        self.ui.Btn_input2.setText(str(self.Last_Num[1]))

    def yihuo(self, str):
        length = len(str)
        temp = 0
        for i in range(length):
            temp = temp ^ str[i]
        return temp

    def machine(self, str):
        if self.yihuo(str) == 0:
            str[str.index(max(str))] -= 1
            return str
        else:
            length = len(str)
            for i in range(length):
                for j in range(str[i]):
                    temp = str[:]
                    temp[i] = j
                    if self.yihuo(temp) == 0:
                        return temp

    def OnClick_OK(self):
        try:
            num1 = int(self.ui.Btn_input1.text())
            num2 = int(self.ui.Btn_input2.text())
            num3 = int(self.ui.Btn_input3.text())
            temp = [num1, num2, num3]
            if sum(temp) == 0:
                QMessageBox.information(self, 'result', 'player won')

            num = self.machine(temp)
            self.ui.Btn_num1.setText(str(num[0]))
            self.ui.Btn_num2.setText(str(num[1]))
            self.ui.Btn_num3.setText(str(num[2]))
            if sum(num) == 0:
                QMessageBox.information(self, 'result', 'machine won')
            self.Last_Num = num[:]
        except:
            QMessageBox.warning(self, 'warning', '请输入石头数量')

    def signalCall(self, string):
        self.ui.Btn_num1.setText(str(string[0]))
        self.ui.Btn_num2.setText(str(string[1]))
        self.ui.Btn_num3.setText(str(string[2]))
        self.num_temp = string[0:3]
        self.f_s = string[3]
        self.Last_Num = self.num_temp[:]

class UI:
    def __init__(self):
        app = QApplication(sys.argv)

        f1 = Ui_Frame1()
        f2 = Ui_Frame2()
        f3 = Ui_Frame3()
        f1.next = f2
        f2.next = f3
        f2.signal.connect(f3.signalCall)
        f1.show()

        sys.exit(app.exec_())


if __name__ == "__main__":
    UI()