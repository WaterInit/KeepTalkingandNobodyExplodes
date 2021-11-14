from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout, QLineEdit, QCheckBox, QLabel
from PyQt5.QtGui import QIcon, QIntValidator, QFont, QPainter, QColor
from PyQt5.QtCore import Qt
import sys


class Wires(QWidget):
    def __init__(self, text_last_dig_sn):
        super(Wires, self).__init__()
        self.text_last_dig_sn = text_last_dig_sn
        self.setMinimumSize(400, 400)
        self.initUI()


    def initUI(self):
        # Meta
        self.setWindowTitle("Wires")
        self.setGeometry(400, 400, 300, 260)

        label_red = QLabel("Red", self)
        label_red.move(55, 10)
        label_red.setStyleSheet("background-color: red")
        label_white = QLabel("white", self)
        label_white.move(90, 10)
        label_white.setStyleSheet("background-color: white")
        label_blue = QLabel("blue", self)
        label_blue.move(130, 10)
        label_blue.setStyleSheet("background-color: blue")
        label_yellow = QLabel("yellow", self)
        label_yellow.move(160, 10)
        label_yellow.setStyleSheet("background-color: yellow")
        label_black = QLabel("black", self)
        label_black.move(205, 10)
        label_black.setStyleSheet("background-color: black")

        self.label_answer = QLabel("Answer", self)
        self.label_answer.move(10, 180)
        self.label_answer.resize(200, 40)


        # Wire 1
        self.wire_1 = QLabel("Wire 1", self)
        self.wire_1.move(10, 30)
        self.wire_1_checkbox_red = QCheckBox("", self)
        self.wire_1_checkbox_red.move(60, 30)
        self.wire_1_checkbox_white = QCheckBox("", self)
        self.wire_1_checkbox_white.move(100, 30)
        self.wire_1_checkbox_blue = QCheckBox("", self)
        self.wire_1_checkbox_blue.move(138, 30)
        self.wire_1_checkbox_yellow = QCheckBox("", self)
        self.wire_1_checkbox_yellow.move(175, 30)
        self.wire_1_checkbox_black = QCheckBox("", self)
        self.wire_1_checkbox_black.move(212, 30)


        # Wire 2
        self.wire_2 = QLabel("Wire 2", self)
        self.wire_2.move(10, 50)
        self.wire_2_checkbox_red = QCheckBox("", self)
        self.wire_2_checkbox_red.move(60, 50)
        self.wire_2_checkbox_white = QCheckBox("", self)
        self.wire_2_checkbox_white.move(100, 50)
        self.wire_2_checkbox_blue = QCheckBox("", self)
        self.wire_2_checkbox_blue.move(138, 50)
        self.wire_2_checkbox_yellow = QCheckBox("", self)
        self.wire_2_checkbox_yellow.move(175, 50)
        self.wire_2_checkbox_black = QCheckBox("", self)
        self.wire_2_checkbox_black.move(212, 50)
        # Wire 3
        self.wire_3 = QLabel("Wire 3", self)
        self.wire_3.move(10, 70)
        self.wire_3_checkbox_red = QCheckBox("", self)
        self.wire_3_checkbox_red.move(60, 70)
        self.wire_3_checkbox_white = QCheckBox("", self)
        self.wire_3_checkbox_white.move(100, 70)
        self.wire_3_checkbox_blue = QCheckBox("", self)
        self.wire_3_checkbox_blue.move(138, 70)
        self.wire_3_checkbox_yellow = QCheckBox("", self)
        self.wire_3_checkbox_yellow.move(175, 70)
        self.wire_3_checkbox_black = QCheckBox("", self)
        self.wire_3_checkbox_black.move(212, 70)
        # Wire 4
        self.wire_4 = QLabel("Wire 4", self)
        self.wire_4.move(10, 90)
        self.wire_4_checkbox_red = QCheckBox("", self)
        self.wire_4_checkbox_red.move(60, 90)
        self.wire_4_checkbox_white = QCheckBox("", self)
        self.wire_4_checkbox_white.move(100, 90)
        self.wire_4_checkbox_blue = QCheckBox("", self)
        self.wire_4_checkbox_blue.move(138, 90)
        self.wire_4_checkbox_yellow = QCheckBox("", self)
        self.wire_4_checkbox_yellow.move(175, 90)
        self.wire_4_checkbox_black = QCheckBox("", self)
        self.wire_4_checkbox_black.move(212, 90)
        # Wire 5
        self.wire_5 = QLabel("Wire 5", self)
        self.wire_5.move(10, 110)
        self.wire_5_checkbox_red = QCheckBox("", self)
        self.wire_5_checkbox_red.move(60, 110)
        self.wire_5_checkbox_white = QCheckBox("", self)
        self.wire_5_checkbox_white.move(100, 110)
        self.wire_5_checkbox_blue = QCheckBox("", self)
        self.wire_5_checkbox_blue.move(138, 110)
        self.wire_5_checkbox_yellow = QCheckBox("", self)
        self.wire_5_checkbox_yellow.move(175, 110)
        self.wire_5_checkbox_black = QCheckBox("", self)
        self.wire_5_checkbox_black.move(212, 110)
        # Wire 6
        self.wire_6 = QLabel("Wire 6", self)
        self.wire_6.move(10, 130)
        self.wire_6_checkbox_red = QCheckBox("", self)
        self.wire_6_checkbox_red.move(60, 130)
        self.wire_6_checkbox_white = QCheckBox("", self)
        self.wire_6_checkbox_white.move(100, 130)
        self.wire_6_checkbox_blue = QCheckBox("", self)
        self.wire_6_checkbox_blue.move(138, 130)
        self.wire_6_checkbox_yellow = QCheckBox("", self)
        self.wire_6_checkbox_yellow.move(175, 130)
        self.wire_6_checkbox_black = QCheckBox("", self)
        self.wire_6_checkbox_black.move(212, 130)

        # Accept Button
        self.acceptButton = QPushButton(self)
        self.acceptButton.setText("Solve")
        self.acceptButton.clicked.connect(lambda: self.solve())
        self.acceptButton.setToolTip("Solve Mystery")
        self.acceptButton.move(100, 150)

        # show variables from before
        label_red = QLabel("last Dig: " + str(self.text_last_dig_sn), self)
        label_red.move(10, 230)

        # Close Button
        self.closeButton = QPushButton(self)
        self.closeButton.setText("Close")  # text
        self.closeButton.setIcon(QIcon("close.png"))  # icon
        self.closeButton.setShortcut('Ctrl+D')  # shortcut key
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setToolTip("Close the widget")  # Tool tip
        self.closeButton.move(210, 230)

    def solve(self):
        print("Solve Mystery")

        # array
        self.wire_checked = [0, 0, 0, 0, 0, 0]  # red = 16, white = 8, blue = 4, yellow = 2, black = 1
        # wire 1
        if (self.wire_1_checkbox_red.isChecked()):
            self.wire_checked[0] += 16
        if (self.wire_1_checkbox_white.isChecked()):
            self.wire_checked[0] += 8
        if (self.wire_1_checkbox_blue.isChecked()):
            self.wire_checked[0] += 4
        if (self.wire_1_checkbox_yellow.isChecked()):
            self.wire_checked[0] += 2
        if (self.wire_1_checkbox_black.isChecked()):
            self.wire_checked[0] += 1
        # wire 2
        if (self.wire_2_checkbox_red.isChecked()):
            self.wire_checked[1] += 16
        if (self.wire_2_checkbox_white.isChecked()):
            self.wire_checked[1] += 8
        if (self.wire_2_checkbox_blue.isChecked()):
            self.wire_checked[1] += 4
        if (self.wire_2_checkbox_yellow.isChecked()):
            self.wire_checked[1] += 2
        if (self.wire_2_checkbox_black.isChecked()):
            self.wire_checked[1] += 1
        # wire 3
        if (self.wire_3_checkbox_red.isChecked()):
            self.wire_checked[2] += 16
        if (self.wire_3_checkbox_white.isChecked()):
            self.wire_checked[2] += 8
        if (self.wire_3_checkbox_blue.isChecked()):
            self.wire_checked[2] += 4
        if (self.wire_3_checkbox_yellow.isChecked()):
            self.wire_checked[2] += 2
        if (self.wire_3_checkbox_black.isChecked()):
            self.wire_checked[2] += 1
        # wire 4
        if (self.wire_4_checkbox_red.isChecked()):
            self.wire_checked[3] += 16
        if (self.wire_4_checkbox_white.isChecked()):
            self.wire_checked[3] += 8
        if (self.wire_4_checkbox_blue.isChecked()):
            self.wire_checked[3] += 4
        if (self.wire_4_checkbox_yellow.isChecked()):
            self.wire_checked[3] += 2
        if (self.wire_4_checkbox_black.isChecked()):
            self.wire_checked[3] += 1
        # wire 5
        if (self.wire_5_checkbox_red.isChecked()):
            self.wire_checked[4] += 16
        if (self.wire_5_checkbox_white.isChecked()):
            self.wire_checked[4] += 8
        if (self.wire_5_checkbox_blue.isChecked()):
            self.wire_checked[4] += 4
        if (self.wire_5_checkbox_yellow.isChecked()):
            self.wire_checked[4] += 2
        if (self.wire_5_checkbox_black.isChecked()):
            self.wire_checked[4] += 1
        # wire 6
        if (self.wire_6_checkbox_red.isChecked()):
            self.wire_checked[5] += 16
        if (self.wire_6_checkbox_white.isChecked()):
            self.wire_checked[5] += 8
        if (self.wire_6_checkbox_blue.isChecked()):
            self.wire_checked[5] += 4
        if (self.wire_6_checkbox_yellow.isChecked()):
            self.wire_checked[5] += 2
        if (self.wire_6_checkbox_black.isChecked()):
            self.wire_checked[5] += 1

        # count Wires
        count_wires = 0
        for wire in self.wire_checked:
            if wire > 0:
                count_wires += 1

        print("Wires: " + str(count_wires))

        solve_text = "error"
        if (count_wires < 3) or (count_wires > 6):
            print("error. Can only be between 3-6 Wires. But you enter " + str(count_wires) + " Wires")
        elif count_wires == 3:
            solve_text = self.wires_3()
        elif count_wires == 4:
            solve_text = self.wires_4()
        elif count_wires == 5:
            solve_text = self.wires_5()
        elif count_wires == 6:
            solve_text = self.wires_6()

        self.label_answer.setText(solve_text)


        #self.wire_checked = [0, 0, 0, 0, 0, 0]  # red = 16, white = 8, blue = 4, yellow = 2, black = 1

    def wires_6(self):
        print("6 Wires")
        print(self.wire_checked)
        # first
        count_wires_yellow = 0
        for wire in self.wire_checked:
            if wire == 2:
                count_wires_yellow += 1
        if not (int(self.text_last_dig_sn) % 2 == 0):
            if count_wires_yellow == 0:
                return("cut the third wire")
        # second
        count_wires_white = 0
        for wire in self.wire_checked:
            if wire == 8:
                count_wires_white += 1
        if (count_wires_yellow == 1) and (count_wires_white > 1):
            return ("cut the fourth wire")
        # third
        count_wires_red = 0
        for wire in self.wire_checked:
            if wire == 16:
                count_wires_red += 1
        if count_wires_red == 0:
            return ("cut the last wire")
        # fourth
        return ("cut the fourth wire")

    def wires_5(self):
        print("5 Wires")
        print(self.wire_checked)
        # first
        if not (int(self.text_last_dig_sn) % 2 == 0):
            for wire in reversed(self.wire_checked):  # go through loop from last element to first
                if wire > 0:  # found last wire
                    if wire == 1:  # last wire is black
                        return ("cut the fourth wire")
                    else:  # stop loop if last wire is not white
                        break
        # second
        count_wires_red = 0
        for wire in self.wire_checked:
            if wire == 16:
                count_wires_red += 1
        count_wires_yellow = 0
        for wire in self.wire_checked:
            if wire == 2:
                count_wires_yellow += 1
        if (count_wires_red == 1) and (count_wires_yellow > 1):
            return("cut the first wire")
        # third
        count_wires_black = 0
        for wire in self.wire_checked:
            if wire == 1:
                count_wires_black += 1
        if count_wires_black == 0:
            return("cut the second wire")
        # fourth
        return("cut the first wire")

    def wires_4(self):
        print("4 Wires")
        print(self.wire_checked)
        # first
        count_wires_red = 0
        for wire in self.wire_checked:
            if wire == 16:
                count_wires_red += 1
        if count_wires_red > 1:
            if not (int(self.text_last_dig_sn) % 2 == 0):
                return("cut the last red wire")
        # second
        if count_wires_red == 0:
            for wire in reversed(self.wire_checked):  # go through loop from last element to first
                if wire > 0:  # found last wire
                    if wire == 2:  # last wire is white
                        return ("cut the first wire")
                    else:  # stop loop if last wire is not white
                        break
        # third
        count_wires_blue = 0
        for wire in self.wire_checked:
            if wire == 4:
                count_wires_blue += 1
        if count_wires_blue == 1:
            return("cut the first wire")
        # fourth
        count_wires_yellow = 0
        for wire in self.wire_checked:
            if wire == 2:
                count_wires_yellow += 1
        if count_wires_yellow > 1:
            return("cut the last wire")
        # fifth
        return("cut the second wire")


    def wires_3(self):
        print("3 Wires")
        # first line
        count_wires_red = 0
        for wire in self.wire_checked:
            if wire == 16:
                count_wires_red += 1
        if count_wires_red == 0:
            return("Cut the second Wire")
        # second line
        for wire in reversed(self.wire_checked):  # go through loop from last element to first
            if wire > 0:  # found last wire
                if wire == 8:  # last wire is white
                    return ("cut the last wire")
                else:  # stop loop if last wire is not white
                    break
        # third line
        count_blue_wires = 0
        for wire in self.wire_checked:
            if wire == 4:
                count_blue_wires += 1
        if count_blue_wires > 1:
            return("Cut the last blue wire")
        # fourth line
        return("Cut the last wire")

