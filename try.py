from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configurations")
        self.setGeometry(400, 400, 700, 400)

        # Horizontal layout for the label number of sensors and textbox and enter button
        self.horizontal_layout1 = QHBoxLayout()

        self.vertical_layout = QVBoxLayout()

        # Horizontal layout for submit and clear buttons
        self.horizontal_layout2 = QHBoxLayout()

        # Parent layout for any layout in the class
        self.layout = QVBoxLayout()

        # Adding the horizontal_layout1 and horizontal_layout2 to the parent layout
        self.layout.addLayout(self.horizontal_layout1)
        self.layout.addLayout(self.vertical_layout)
        self.layout.addLayout(self.horizontal_layout2)

        # Setting the parent layout as the main layout
        container = QWidget()
        container.setLayout(self.layout)
        self.setMenuWidget(container)


        # Open in full screen
        self.showMaximized()

    def label(self, text):
        label = QLabel (text, self)
        label.setFont(QtGui.QFont('Arial', 15)) 
        label.adjustSize()
        self.horizontal_layout1.addWidget(label)

    def textBox(self):
        self.textbox = QLineEdit(self)
        self.horizontal_layout1.addWidget(self.textbox)

    def enter_button(self):
        pb = QPushButton()
        pb.setText("Enter")
        self.horizontal_layout1.addWidget(pb)
        pb.clicked.connect(self.sensors)   

    def button(self, text):
        pb = QPushButton()
        pb.setText(text)
        self.horizontal_layout2.addWidget(pb)
        return pb
        
    def sensors(self):
        self.previous_layout = None
        number_of_sensors = int(self.textbox.text())
        if (self.previous_layout != None):
            # for i in range (self.previous_layout.count()):
            self.previous_layout.itemAt(0).widget().deleteLater()
        for i in range(number_of_sensors):
            sensors_combobox = QComboBox()
            sensors_combobox.addItems(['zeby'])
            self.vertical_layout.addWidget(sensors_combobox)
        self.layout.addLayout(self.vertical_layout)
        self.previous_layout = self.vertical_layout

    def button_click(self):
        number_of_sensors = self.textbox.text
        print (number_of_sensors)

app = QApplication(sys.argv)
w = MainWindow()
w.label("Number of sensors")
w.textBox()
w.enter_button()
submit = w.button("Submit")
clear = w.button("Clear")
w.show()
app.exec_()