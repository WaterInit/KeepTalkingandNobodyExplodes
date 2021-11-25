from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout, QLineEdit, QCheckBox, QLabel, QMainWindow
from PyQt5.QtGui import QIcon, QIntValidator, QFont, QPainter, QColor, QPixmap
from PyQt5.QtCore import Qt
import sys


class Memory(QWidget):
    def __init__(self):
        super(Memory, self).__init__()
        self.setMinimumSize(150, 480)
        self.initUI()


    def initUI(self):
        # Meta
        self.setWindowTitle("Memory")
        self.setGeometry(400, 400, 300, 260)

        # stage 1
        self.stage_1 = QLabel("Stage 1", self)
        self.stage_1.move(40, 30)
        self.stage_1_label = QLabel("label", self)
        self.stage_1_label.move(10, 50)
        self.stage_1_label_input = QLineEdit(self)
        self.stage_1_label_input.move(15, 70)
        self.stage_1_label_input.resize(20, 20)
        self.stage_1_position = QLabel("position", self)
        self.stage_1_position.move(70, 50)
        self.stage_1_position_inoput = QLineEdit(self)
        self.stage_1_position_inoput.move(75, 70)
        self.stage_1_position_inoput.resize(20, 20)
        # stage 2
        self.stage_2 = QLabel("Stage 2", self)
        self.stage_2.move(40, 110)
        self.stage_2_label = QLabel("label", self)
        self.stage_2_label.move(10, 130)
        self.stage_2_label_input = QLineEdit(self)
        self.stage_2_label_input.move(15, 150)
        self.stage_2_label_input.resize(20, 20)
        self.stage_2_position = QLabel("position", self)
        self.stage_2_position.move(70, 130)
        self.stage_2_position_inoput = QLineEdit(self)
        self.stage_2_position_inoput.move(75, 150)
        self.stage_2_position_inoput.resize(20, 20)
        # stage 3
        self.stage_3 = QLabel("Stage 3", self)
        self.stage_3.move(40, 190)
        self.stage_3_label = QLabel("label", self)
        self.stage_3_label.move(10, 210)
        self.stage_3_label_input = QLineEdit(self)
        self.stage_3_label_input.move(15, 230)
        self.stage_3_label_input.resize(20, 20)
        self.stage_3_position = QLabel("position", self)
        self.stage_3_position.move(70, 210)
        self.stage_3_position_inoput = QLineEdit(self)
        self.stage_3_position_inoput.move(75, 230)
        self.stage_3_position_inoput.resize(20, 20)
        # stage 4
        self.stage_4 = QLabel("Stage 4", self)
        self.stage_4.move(40, 270)
        self.stage_4_label = QLabel("label", self)
        self.stage_4_label.move(10, 290)
        self.stage_4_label_input = QLineEdit(self)
        self.stage_4_label_input.move(15, 310)
        self.stage_4_label_input.resize(20, 20)
        self.stage_4_position = QLabel("position", self)
        self.stage_4_position.move(70, 290)
        self.stage_4_position_inoput = QLineEdit(self)
        self.stage_4_position_inoput.move(75, 310)
        self.stage_4_position_inoput.resize(20, 20)
        # stage 5
        self.stage_5 = QLabel("Stage 5", self)
        self.stage_5.move(40, 350)
        self.stage_5_label = QLabel("label", self)
        self.stage_5_label.move(10, 370)
        self.stage_5_label_input = QLineEdit(self)
        self.stage_5_label_input.move(15, 390)
        self.stage_5_label_input.resize(20, 20)
        self.stage_5_position = QLabel("position", self)
        self.stage_5_position.move(70, 370)
        self.stage_5_position_inoput = QLineEdit(self)
        self.stage_5_position_inoput.move(75, 390)
        self.stage_5_position_inoput.resize(20, 20)

        # Close Button
        self.closeButton = QPushButton(self)
        self.closeButton.setText("Close")  # text
        self.closeButton.setIcon(QIcon("close.png"))  # icon
        self.closeButton.setShortcut('Ctrl+D')  # shortcut key
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setToolTip("Close the widget")  # Tool tip
        self.closeButton.move(40, 440)
