from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout, QLineEdit, QCheckBox, QLabel, QMainWindow
from PyQt5.QtGui import QIcon, QIntValidator, QFont, QPainter, QColor, QPixmap
from PyQt5.QtCore import Qt
import sys


class Keypad(QWidget):
    def __init__(self):
        super(Keypad, self).__init__()
        self.setMinimumSize(480, 620)
        self.initUI()


    def initUI(self):
        # Meta
        self.setWindowTitle("Keypad")
        self.setGeometry(400, 400, 300, 260)

        self.label_keys = QLabel("keys", self)
        self.label_keys.move(10, 10)
        # first row
        self.archaic_koppa = QCheckBox("\u03d8  - Archaic Koppa", self)
        self.archaic_koppa.move(50, 10)
        self.little_yus = QCheckBox("\u0466  - little Yus", self)
        self.little_yus.move(50, 30)
        self.lambda_bar = QCheckBox("\u019b  - lambda-bar", self)
        self.lambda_bar.move(50, 50)
        self.kappa = QCheckBox("\u03DE  - Kappa", self)
        self.kappa.move(50, 70)
        self.bigyus = QCheckBox("\u046d  - big Yus", self)
        self.bigyus.move(50, 90)
        self.greek_kai = QCheckBox("\u03d7  - greek Kai", self)
        self.greek_kai.move(50, 110)
        self.reversed_sigma = QCheckBox("\u03ff  - reversed Sigma", self)
        self.reversed_sigma.move(50, 130)
        # second row
        self.backward_e = QCheckBox("\u2108 with 2 points above  - backward e", self)
        self.backward_e.move(50, 150)
        self.ha = QCheckBox("\u04a9  - ha", self)
        self.ha.move(50, 170)
        self.white_star = QCheckBox("\u2606  - white star", self)
        self.white_star.move(50, 190)
        self.inverted_question_mark = QCheckBox("\u00bf  - inverted question mark", self)
        self.inverted_question_mark.move(50, 210)
        # third row
        self.copyright = QCheckBox("\u00a9  - Copyright", self)
        self.copyright.move(50, 230)
        self.w = QCheckBox("W with ^,", self)
        self.w.move(50, 250)
        self.zhe_descender = QCheckBox("\u0496  - zhe descender", self)
        self.zhe_descender.move(50, 270)
        self.komi_dzje = QCheckBox("\u0507  - Komi Dzje", self)
        self.komi_dzje.move(50, 290)
        # fourth row
        self.shima = QCheckBox("\u03ec  - Shima", self)
        self.shima.move(50, 310)
        self.pilcrow = QCheckBox("\u00b6  - Pilcrow", self)
        self.pilcrow.move(50, 330)
        self.yat = QCheckBox("\u0463  - Yat", self)
        self.yat.move(50, 350)
        self.smile_tongue = QCheckBox("\u062a  - smile with tongue", self)
        self.smile_tongue.move(50, 370)
        # fifth row
        self.psi = QCheckBox("\u03a8  - Psi", self)
        self.psi.move(50, 390)
        self.sigma = QCheckBox("\u03fe  - sigma", self)
        self.sigma.move(50, 410)
        self.ksi = QCheckBox("\u046e  - Ksi", self)
        self.ksi.move(50, 430)
        self.black_star = QCheckBox("\u2605  - black star", self)
        self.black_star.move(50, 450)
        # sixth row (last)
        self.puzzle = QCheckBox("Puzzle", self)
        self.puzzle.move(50, 470)
        self.ae = QCheckBox("\u00e6  - ae", self)
        self.ae.move(50, 490)
        self.i_with_tail = QCheckBox("\u048a  - I with tail", self)
        self.i_with_tail.move(50, 510)
        self.omega = QCheckBox("\u03a9  - Omega", self)
        self.omega.move(50, 530)

        # result
        self.result_1 = QCheckBox("1. Sign", self)
        self.result_1.move(300, 50)
        self.result_1.resize(200, 40)
        self.result_2 = QCheckBox("2. Sign", self)
        self.result_2.move(300, 70)
        self.result_2.resize(200, 40)
        self.result_3 = QCheckBox("3. Sign", self)
        self.result_3.move(300, 90)
        self.result_3.resize(200, 40)
        self.result_4 = QCheckBox("4. Sign", self)
        self.result_4.move(300, 110)
        self.result_4.resize(200, 40)
        self.result_5 = QCheckBox("5. Sign", self)
        self.result_5.move(300, 130)
        self.result_5.resize(200, 40)
        self.result_6 = QCheckBox("6. Sign", self)
        self.result_6.move(300, 150)
        self.result_6.resize(200, 40)
        self.result_7 = QCheckBox("7. Sign", self)
        self.result_7.move(300, 170)
        self.result_7.resize(200, 40)


        # Accept Button
        self.acceptButton = QPushButton(self)
        self.acceptButton.setText("Solve")
        self.acceptButton.clicked.connect(lambda: self.solve())
        self.acceptButton.setToolTip("Solve Mystery")
        self.acceptButton.move(100, 580)


        # Close Button
        self.closeButton = QPushButton(self)
        self.closeButton.setText("Close")  # text
        self.closeButton.setIcon(QIcon("close.png"))  # icon
        self.closeButton.setShortcut('Ctrl+D')  # shortcut key
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setToolTip("Close the widget")  # Tool tip
        self.closeButton.move(260, 580)


    def solve(self):
        print("solve")
        row_1 = [self.archaic_koppa, self.little_yus, self.lambda_bar, self.kappa, self.bigyus, self.greek_kai,
                 self.reversed_sigma]
        row_2 = [self.backward_e, self.archaic_koppa, self.reversed_sigma, self.ha, self.white_star, self.greek_kai,
                 self.inverted_question_mark]
        row_3 = [self.copyright, self.w, self.ha, self.zhe_descender, self.komi_dzje, self.lambda_bar, self.white_star]
        row_4 = [self.shima, self.pilcrow, self.yat, self.bigyus, self.zhe_descender, self.inverted_question_mark,
                 self.smile_tongue]
        row_5 = [self.psi, self.smile_tongue, self.yat, self.sigma, self.pilcrow, self.ksi, self.black_star]
        row_6 = [self.shima, self.backward_e, self.puzzle, self.ae, self.psi, self.i_with_tail, self.omega]

        rows = [row_1, row_2, row_3, row_4, row_5, row_6]
        for row in rows:
            count_4 = 0
            for sign in row:
                if sign.isChecked():
                    count_4 += 1
            if count_4 is 4:
                print("Ergebnis")
                self.result_1.setText((row[0].text()))
                self.result_2.setText((row[1].text()))
                self.result_3.setText((row[2].text()))
                self.result_4.setText((row[3].text()))
                self.result_5.setText((row[4].text()))
                self.result_6.setText((row[5].text()))
                self.result_7.setText((row[6].text()))
                break;

