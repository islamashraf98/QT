from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configurations")
        self.setGeometry(400, 400, 700, 400)

        # Horizontal layout for the label number of sensors and textbox
        self.horizontal_layout = QHBoxLayout()

        # Parent layout for any layout in the class
        self.layout = QVBoxLayout()

        # Adding the horizontal_layout to the parent layout
        self.layout.addLayout(self.horizontal_layout)

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
        self.horizontal_layout.addWidget(label)

    def textBox(self):
        self.textbox = QLineEdit(self)
        self.horizontal_layout.addWidget(self.textbox)

    def button(self):
        pb = QPushButton()
        pb.setText("Enter")
        self.horizontal_layout.addWidget(pb)
        pb.clicked.connect(self.sensors)   

    def sensors(self):
        self.previous_layout = None
        number_of_sensors = int(self.textbox.text())
        vlayout = QVBoxLayout()
        if (self.previous_layout != None):
            for i in range (self.previous_layout.count()):
                self.previous_layout.removeWidget(self.previous_layout.itemAt(i))
        for i in range(number_of_sensors):
            sensors_combobox = QComboBox()
            sensors_combobox.addItems(['zeby'])
            vlayout.addWidget(sensors_combobox)
        self.layout.addLayout(vlayout)
        self.previous_layout = vlayout

    def button_click(self):
        number_of_sensors = self.textbox.text
        print (number_of_sensors)

app = QApplication(sys.argv)
w = MainWindow()
w.label("Number of sensors")
w.textBox()
w.button()
w.show()
app.exec_()