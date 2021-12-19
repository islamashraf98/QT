from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(None)
        self.layout = QVBoxLayout(self)
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText('Enter a color')
        self.line_edit.setStyleSheet('QLineEdit {background-color:white}')
        self.layout.addWidget(self.line_edit)
        self.line_edit.textEdited.connect(self.sensors)
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    # def change_background(self):
    #     col = self.line_edit.text()
    #     self.setStyleSheet(f'QWidget {{background-color: {col};}}')
    #     self.line_edit.clear()

    def sensors(self):
        for i in range(int(self.line_edit.text())):
            print(i)
            hlayout = QHBoxLayout()

            combobox1 = QComboBox()
            combobox1.addItems(['zeby'])

            combobox2 = QComboBox()
            combobox2.addItems(['omar'])

            hlayout.addWidget(combobox1)
            hlayout.addWidget(combobox2)
            self.layout.addLayout(hlayout)



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
