from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout, QLineEdit, QCheckBox, QLabel
from PyQt5.QtGui import QIcon, QIntValidator, QFont, QPainter, QColor
from PyQt5.QtCore import Qt
import sys

from wires import Wires


class MainMenu(QWidget):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.initUI()

    def initUI(self):
        # Meta
        self.setWindowTitle("Main Menu")
        self.setGeometry(400, 400, 300, 260)
        # Wires
        self.wires = QPushButton(self)
        self.wires.setText("Wires")          #text
        self.wires.setIcon(QIcon("close.png")) #icon
        self.wires.clicked.connect(lambda: self.start_mystery("Wires"))
        self.wires.setToolTip("Start Wires") #Tool tip
        self.wires.move(5, 5)
        # Advanced Wires
        self.advanced_wires = QPushButton(self)
        self.advanced_wires.setText("Advanced Wires")          #text
        self.advanced_wires.setIcon(QIcon("close.png")) #icon
        self.advanced_wires.clicked.connect(self.close)
        self.advanced_wires.setToolTip("Start Afvanced Wires") #Tool tip
        self.advanced_wires.move(100, 5)

        # Close Button
        self.closeButton = QPushButton(self)
        self.closeButton.setText("Close")          #text
        self.closeButton.setIcon(QIcon("close.png")) #icon
        self.closeButton.setShortcut('Ctrl+D')  #shortcut key
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setToolTip("Close the widget") #Tool tip
        self.closeButton.move(210, 230)

    def start_mystery(self, mysteryname):
        if mysteryname == "Wires":
            self.myst = Wires()
            self.myst.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenu()
    ex.show()
    sys.exit(app.exec_())
