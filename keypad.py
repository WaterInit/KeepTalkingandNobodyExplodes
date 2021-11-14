from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout, QLineEdit, QCheckBox, QLabel
from PyQt5.QtGui import QIcon, QIntValidator, QFont, QPainter, QColor
from PyQt5.QtCore import Qt
import sys


class Keypad(QWidget):
    def __init__(self):
        super(Keypad, self).__init__()
        self.setMinimumSize(420, 620)
        self.initUI()


    def initUI(self):
        # Meta
        self.setWindowTitle("Keypad")
        self.setGeometry(400, 400, 300, 260)

        self.label_keys = QLabel("keys", self)
        self.label_keys.move(10, 10)
        self.box_keys_1 = QCheckBox("O with leg downwards", self)
        self.box_keys_1.move(50, 10)
        self.box_keys_2 = QCheckBox("A with leg straight down", self)
        self.box_keys_2.move(50, 30)
        self.box_keys_3 = QCheckBox("lambda", self)
        self.box_keys_3.move(50, 50)
        self.box_keys_4 = QCheckBox("N with round edges", self)
        self.box_keys_4.move(50, 70)
        self.box_keys_5 = QCheckBox("triangle with three legs and a shield to the left", self)
        self.box_keys_5.move(50, 90)
        self.box_keys_6 = QCheckBox("H swingt and with round edges", self)
        self.box_keys_6.move(50, 110)
        self.box_keys_7 = QCheckBox("C backwards and with a point in the middle", self)
        self.box_keys_7.move(50, 130)
        self.box_keys_8 = QCheckBox("E backwards with two points about", self)
        self.box_keys_8.move(50, 150)
        self.box_keys_9 = QCheckBox("@ close to", self)
        self.box_keys_9.move(50, 170)
        self.box_keys_10 = QCheckBox("star, empty", self)
        self.box_keys_10.move(50, 190)
        self.box_keys_11 = QCheckBox("? but turned around", self)
        self.box_keys_11.move(50, 210)
        self.box_keys_12 = QCheckBox("Copyright", self)
        self.box_keys_12.move(50, 230)
        self.box_keys_13 = QCheckBox("W with line and , above", self)
        self.box_keys_13.move(50, 250)
        self.box_keys_14 = QCheckBox("X with vertical line in middle", self)
        self.box_keys_14.move(50, 270)
        self.box_keys_15 = QCheckBox("3 without the button part", self)
        self.box_keys_15.move(50, 290)
        self.box_keys_16 = QCheckBox("6", self)
        self.box_keys_16.move(50, 310)
        self.box_keys_17 = QCheckBox("Paragraph", self)
        self.box_keys_17.move(50, 330)
        self.box_keys_18 = QCheckBox("b with T inside", self)
        self.box_keys_18.move(50, 350)
        self.box_keys_19 = QCheckBox("smilie", self)
        self.box_keys_19.move(50, 370)
        self.box_keys_20 = QCheckBox("C with point inside", self)
        self.box_keys_20.move(50, 390)
        self.box_keys_21 = QCheckBox("3 with antennas and line underneath", self)
        self.box_keys_21.move(50, 410)
        self.box_keys_22 = QCheckBox("star, black", self)
        self.box_keys_22.move(50, 430)
        self.box_keys_23 = QCheckBox("3 with 2 Points above", self)
        self.box_keys_23.move(50, 450)
        self.box_keys_24 = QCheckBox("Puzzle", self)
        self.box_keys_24.move(50, 470)
        self.box_keys_25 = QCheckBox("ae", self)
        self.box_keys_25.move(50, 490)
        self.box_keys_26 = QCheckBox("Y with a vertical line", self)
        self.box_keys_26.move(50, 510)
        self.box_keys_27 = QCheckBox("N turned around with line above and at the right bottom", self)
        self.box_keys_27.move(50, 530)
        self.box_keys_28 = QCheckBox("Omega (big)", self)
        self.box_keys_28.move(50, 550)




        # Close Button
        self.closeButton = QPushButton(self)
        self.closeButton.setText("Close")  # text
        self.closeButton.setIcon(QIcon("close.png"))  # icon
        self.closeButton.setShortcut('Ctrl+D')  # shortcut key
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setToolTip("Close the widget")  # Tool tip
        self.closeButton.move(210, 580)
