from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout, QLineEdit, QCheckBox, QLabel
from PyQt5.QtGui import QIcon, QIntValidator, QFont, QPainter, QColor
from PyQt5.QtCore import Qt
import sys


class Button(QWidget):
    def __init__(self, count_batteries, lid_indicators):
        super(Button, self).__init__()
        self.count_batteries = count_batteries
        self.lid_indicators = lid_indicators
        self.setMinimumSize(400, 400)
        self.initUI()


    def initUI(self):
        # Meta
        self.setWindowTitle("Button")
        self.setGeometry(400, 400, 300, 260)

        print(self.count_batteries)
        print(self.lid_indicators)

        # B. color: blue, white, yellow, red
        # B. says: Abort, Detonate, Hold
        # lid indicators: CAR, FRK
        # count batteries

        # Button color
        label_red = QLabel("blue", self)
        label_red.move(55, 10)
        label_red.setStyleSheet("background-color: blue")
        label_white = QLabel("white", self)
        label_white.move(90, 10)
        label_white.setStyleSheet("background-color: white")
        label_blue = QLabel("yellow", self)
        label_blue.move(125, 10)
        label_blue.setStyleSheet("background-color: yellow")
        label_yellow = QLabel("red", self)
        label_yellow.move(172, 10)
        label_yellow.setStyleSheet("background-color: red")
        # checkboxes
        self.bcolor = QLabel("B. color", self)
        self.bcolor.move(10, 30)
        self.bcolor_checkbox_blue = QCheckBox("", self)
        self.bcolor_checkbox_blue.move(60, 30)
        self.bcolor_checkbox_white = QCheckBox("", self)
        self.bcolor_checkbox_white.move(100, 30)
        self.bcolor_checkbox_yellow = QCheckBox("", self)
        self.bcolor_checkbox_yellow.move(138, 30)
        self.bcolor_checkbox_red = QCheckBox("", self)
        self.bcolor_checkbox_red.move(175, 30)


        # Button says
        label_red = QLabel("Abort", self)
        label_red.move(60, 60)
        label_white = QLabel("Detonate", self)
        label_white.move(100, 60)
        label_blue = QLabel("Hold", self)
        label_blue.move(160, 60)
        # checkboxes
        self.bsays = QLabel("B. says", self)
        self.bsays.move(10, 80)
        self.bsays_checkbox_abort = QCheckBox("", self)
        self.bsays_checkbox_abort.move(70, 80)
        self.bsays_checkbox_detonate = QCheckBox("", self)
        self.bsays_checkbox_detonate.move(122, 80)
        self.bsays_checkbox_hold = QCheckBox("", self)
        self.bsays_checkbox_hold.move(168, 80)



        # answer label field
        self.label_answer = QLabel("Answer", self)
        self.label_answer.move(10, 180)
        self.label_answer.resize(200, 40)

        # Releasing a Held Button
        self.label_release_button_blue = QLabel("Blue strip: release when countdown shows 4", self)
        self.label_release_button_blue.move(10, 220)
        self.label_release_button_blue.resize(300, 40)
        self.label_release_button_white = QLabel("White strip: release when countdown shows 1", self)
        self.label_release_button_white.move(10, 250)
        self.label_release_button_white.resize(300, 40)
        self.label_release_button_yellow = QLabel("Yellow strip: release when countdown shows 5", self)
        self.label_release_button_yellow.move(10, 280)
        self.label_release_button_yellow.resize(300, 40)
        self.label_release_button_other = QLabel("any other strip: release when countdown shows 1", self)
        self.label_release_button_other.move(10, 310)
        self.label_release_button_other.resize(300, 40)


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
        self.closeButton.move(280, 350)


    def solve(self):
        print("Solve Mystery")

        # 1
        if (self.bcolor_checkbox_blue.isChecked()) and (self.bsays_checkbox_abort.isChecked()):
            self.label_answer.setText("Hold Button and see Releasing")
        # 2
        if (int(self.count_batteries) > 1) and (self.bsays_checkbox_detonate.isChecked()):
            self.label_answer.setText("press and immediately release the button")
        # 3
        if (self.bcolor_checkbox_white.isChecked()) and ("car" in self.lid_indicators):
            self.label_answer.setText("Hold Button and see Releasing")
        # 4
        if (int(self.count_batteries) > 2) and ("frk" in self.lid_indicators):
            self.label_answer.setText("press and immediately release the button")
        # 5
        if (self.bcolor_checkbox_yellow.isChecked()):
            self.label_answer.setText("Hold Button and see Releasing")
        # 6
        if (self.bcolor_checkbox_red.isChecked()) and (self.bsays_checkbox_hold.isChecked()):
            self.label_answer.setText("press and immediately release the button")
        # 7
        self.label_answer.setText("Hold Button and see Releasing")
