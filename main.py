from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout, QLineEdit, QCheckBox, QLabel
from PyQt5.QtGui import QIcon, QIntValidator, QFont, QPainter, QColor
from PyQt5.QtCore import Qt
import sys

from wires import Wires
from button import Button
from keypad import Keypad
from memory import Memory

#######################################
# Version 1 #
# Verification Code: 241
#######################################



class MainMenu(QWidget):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.setMinimumSize(400, 400)
        self.initUI()

    def initUI(self):
        # Meta
        self.setWindowTitle("Main Menu")
        self.setGeometry(400, 400, 300, 260)
        #self.setGeometry(500, 500, 300, 260)
        # Advanced Wires
        self.advanced_wires = QPushButton(self)
        self.advanced_wires.setText("Advanced Wires")          #text
        self.advanced_wires.setIcon(QIcon("close.png")) #icon
        self.advanced_wires.clicked.connect(self.close)
        self.advanced_wires.setToolTip("Start Afvanced Wires") #Tool tip
        self.advanced_wires.move(5, 5)
        # Button
        self.button = QPushButton(self)
        self.button.setText("Button")
        self.button.setIcon(QIcon("close.png")) #icon
        self.button.clicked.connect(lambda: self.start_mystery("Button"))
        self.button.setToolTip("Start Button") #Tool tip
        self.button.move(135, 5)
        # Keypad
        self.keypad = QPushButton(self)
        self.keypad.setText("Keypad")
        self.keypad.setIcon(QIcon("close.png")) #icon
        self.keypad.clicked.connect(lambda: self.start_mystery("Keypad"))
        self.keypad.setToolTip("Start Keypad") #Tool tip
        self.keypad.move(220, 5)
        # Wires
        self.wires = QPushButton(self)
        self.wires.setText("Wires")          #text
        self.wires.setIcon(QIcon("close.png")) #icon
        self.wires.clicked.connect(lambda: self.start_mystery("Wires"))
        self.wires.setToolTip("Start Wires") #Tool tip
        self.wires.move(5, 35)
        # Memory
        self.memory = QPushButton(self)
        self.memory.setText("Memory")          #text
        self.memory.setIcon(QIcon("close.png")) #icon
        self.memory.clicked.connect(lambda: self.start_mystery("Memory"))
        self.memory.setToolTip("Start Memory") #Tool tip
        self.memory.move(90, 35)

        ## some start infos ##
        # last digit even or odd
        self.label_last_dig_sn = QLabel("Last Digit of SN", self)
        self.label_last_dig_sn.move(10, 180)
        self.text_last_dig_sn = QLineEdit(self)
        self.text_last_dig_sn.move(110, 180)
        self.text_last_dig_sn.resize(20, 20)
        # count batteries
        self.label_count_batteries = QLabel("count batteries", self)
        self.label_count_batteries.move(10, 210)
        self.text_count_batteries = QLineEdit(self)
        self.text_count_batteries.move(110, 210)
        self.text_count_batteries.resize(20, 20)
        # lid indicators: CAR, FRK
        self.label_lid_indicators = QLabel("lid indicators", self)
        self.label_lid_indicators.move(10, 240)
        self.box_lid_indicator_car = QCheckBox("CAR", self)
        self.box_lid_indicator_car.move(110, 240)
        self.box_lid_indicator_frk = QCheckBox("FRK", self)
        self.box_lid_indicator_frk.move(110, 260)


        # Close Button
        self.closeButton = QPushButton(self)
        self.closeButton.setText("Close")          #text
        self.closeButton.setIcon(QIcon("close.png")) #icon
        self.closeButton.setShortcut('Ctrl+D')  #shortcut key
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setToolTip("Close the widget") #Tool tip
        self.closeButton.move(210, 330)

    def start_mystery(self, mysteryname):
        lid_indicators = []
        if(self.box_lid_indicator_car.isChecked()):
            lid_indicators.append("car")
        if(self.box_lid_indicator_frk.isChecked()):
            lid_indicators.append("frk")

        if mysteryname == "Wires":
            self.myst = Wires(self.text_last_dig_sn.text())
            self.myst.show()
        elif mysteryname == "Button":
            self.myst = Button(self.text_count_batteries.text(), lid_indicators)
            self.myst.show()
        elif mysteryname == "Keypad":
            self.myst = Keypad()
            self.myst.show()
        elif mysteryname == "Memory":
            self.myst = Memory()
            self.myst.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenu()
    ex.show()
    sys.exit(app.exec_())
