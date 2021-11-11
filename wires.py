from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout, QLineEdit, QCheckBox, QLabel
from PyQt5.QtGui import QIcon, QIntValidator, QFont, QPainter, QColor
from PyQt5.QtCore import Qt
import sys


class Wires(QWidget):
    def __init__(self):
        super(Wires, self).__init__()
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

        # Accept Button
        self.acceptButton = QPushButton(self)
        self.acceptButton.setText("Solve")
        self.acceptButton.clicked.connect(lambda: self.solve())
        self.acceptButton.setToolTip("Solve Mystery")
        self.acceptButton.move(100, 150)

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
        # count Wires
        count_wires = 0
        if(self.wire_1_checkbox_red.isChecked() or \
                self.wire_1_checkbox_white.isChecked() or \
                self.wire_1_checkbox_blue.isChecked() or\
                self.wire_1_checkbox_yellow.isChecked() or \
                self.wire_1_checkbox_black.isChecked()):
            count_wires += 1
        if (self.wire_2_checkbox_red.isChecked() or \
                self.wire_2_checkbox_white.isChecked() or \
                self.wire_2_checkbox_blue.isChecked() or \
                self.wire_2_checkbox_yellow.isChecked() or \
                self.wire_2_checkbox_black.isChecked()):
            count_wires += 1
        if (self.wire_3_checkbox_red.isChecked() or \
                self.wire_3_checkbox_white.isChecked() or \
                self.wire_3_checkbox_blue.isChecked() or \
                self.wire_3_checkbox_yellow.isChecked() or \
                self.wire_3_checkbox_black.isChecked()):
            count_wires += 1
        if (self.wire_4_checkbox_red.isChecked() or \
                self.wire_4_checkbox_white.isChecked() or \
                self.wire_4_checkbox_blue.isChecked() or \
                self.wire_4_checkbox_yellow.isChecked() or \
                self.wire_4_checkbox_black.isChecked()):
            count_wires += 1
        if (self.wire_5_checkbox_red.isChecked() or \
                self.wire_5_checkbox_white.isChecked() or \
                self.wire_5_checkbox_blue.isChecked() or \
                self.wire_5_checkbox_yellow.isChecked() or \
                self.wire_5_checkbox_black.isChecked()):
            count_wires += 1
        print("Wires: " + str(count_wires))

        if (count_wires < 3) or (count_wires > 6):
            print("error. Can only be between 3-6 Wires. But you enter " + str(count_wires) + " Wires")
        elif count_wires is 3:
            self.wires_3()

    def wires_3(self):
        print("3 Wires")
        if not (self.wire_1_checkbox_red.isChecked() or \
                self.wire_2_checkbox_red.isChecked() or \
                self.wire_3_checkbox_red.isChecked() or \
                self.wire_4_checkbox_red.isChecked() or \
                self.wire_5_checkbox_red.isChecked()):
            answer_text = ("Cut the second Wire")
        elif (self.wire_5_checkbox_white.isChecked()):
            answer_text = ("Cut the last Wire")
        else:
            count_blue_wires = 0
            if self.wire_1_checkbox_blue.isChecked():
                count_blue_wires += 1
            if self.wire_2_checkbox_blue.isChecked():
                count_blue_wires += 1
            if self.wire_3_checkbox_blue.isChecked():
                count_blue_wires += 1
            if self.wire_4_checkbox_blue.isChecked():
                count_blue_wires += 1
            if self.wire_5_checkbox_blue.isChecked():
                count_blue_wires += 1
            if count_blue_wires > 1:
                answer_text = ("Cut the last blue wire")
            else:
                answer_text = ("Cut the last wire")

        self.label_answer.setText(answer_text)