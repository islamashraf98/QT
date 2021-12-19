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

        # Vertical layout for sensors
        self.vertical_layout = QVBoxLayout()

        # Horizontal layout for camera
        self.horizontal_layout3 = QHBoxLayout()

        # Horizontal layout for submit and clear buttons
        self.horizontal_layout2 = QHBoxLayout()


        # Parent layout for any layout in the class
        self.layout = QVBoxLayout()

        # Adding the children to the parent layout
        self.layout.addLayout(self.horizontal_layout1)
        self.layout.addLayout(self.vertical_layout)
        self.layout.addLayout(self.horizontal_layout3)
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

    def camera(self):
        label = QLabel ("Camera power", self)
        label.setFont(QtGui.QFont('Arial', 10)) 
        label.adjustSize()
        self.yes = QRadioButton("On", self)
        self.no = QRadioButton("Off", self)
        self.horizontal_layout3.addWidget(label)
        self.horizontal_layout3.addWidget(self.yes)
        self.horizontal_layout3.addWidget(self.no)

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
        types_of_sensors = ['ultrasonic', 'temprature', 'speed', 'accelorometer', 'gps']
        number_of_sensors = int(self.textbox.text())
        self.combobox_options = []
        for i in range(number_of_sensors):
            sensors_combobox = QComboBox()
            sensors_combobox.addItems([x for x in types_of_sensors])
            self.vertical_layout.addWidget(sensors_combobox)
            self.combobox_options.append(sensors_combobox)
        self.layout.addLayout(self.vertical_layout)
        self.camera()

    def button_click(self):
        number_of_sensors = self.textbox.text
        print (number_of_sensors)

    def submit_click(self):
        Dict = {}
        length = len(self.combobox_options)
        for i, j in zip(self.combobox_options, range(length)):
            Dict[j] = i.currentText()
        Dict[length] = self.yes.text() if self.yes.isChecked() else self.no.text()
        print (Dict)
            

app = QApplication(sys.argv)
w = MainWindow()
w.label("Number of sensors")
w.textBox()
w.enter_button()
submit = w.button("Submit")
submit.clicked.connect(w.submit_click)
clear = w.button("Clear")
w.show()
app.exec_()