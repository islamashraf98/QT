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
        self.input_layout = QHBoxLayout()

        # Vertical layout for sensors
        self.sensors_layout = QVBoxLayout()

        # Horizontal layout for camera
        self.camera_layout = QHBoxLayout()

        # Horizontal layout for submit and clear buttons
        self.submit_clear_layout = QHBoxLayout()

        # Parent layout for any layout in the class
        self.layout = QVBoxLayout()

        # Adding the children to the parent layout
        self.layout.addLayout(self.input_layout)
        self.layout.addLayout(self.sensors_layout)
        self.sensors_layout.addLayout(self.camera_layout)
        self.layout.addLayout(self.submit_clear_layout)

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
        self.input_layout.addWidget(label)

    def camera(self):
        label = QLabel ("Camera power", self)
        label.setFont(QtGui.QFont('Arial', 10)) 
        label.adjustSize()
        self.yes = QRadioButton("On", self)
        self.no = QRadioButton("Off", self)
        self.camera_layout.addWidget(label)
        self.camera_layout.addWidget(self.yes)
        self.camera_layout.addWidget(self.no)

    def textBox(self):
        self.textbox = QLineEdit(self)
        self.input_layout.addWidget(self.textbox)

    def enter_button(self):
        pb = QPushButton()
        pb.setText("Enter")
        self.input_layout.addWidget(pb)
        pb.clicked.connect(self.sensors)   

    def button(self, text):
        pb = QPushButton()
        pb.setText(text)
        self.submit_clear_layout.addWidget(pb)
        return pb

    def sensors(self):
        types_of_sensors = ['ultrasonic', 'temprature', 'speed', 'accelorometer', 'gps']
        number_of_sensors = int(self.textbox.text())
        self.combobox_options = []
        for i in range(number_of_sensors):
            sensors_combobox = QComboBox()
            sensors_combobox.addItems([x for x in types_of_sensors])
            self.sensors_layout.addWidget(sensors_combobox)
            self.combobox_options.append(sensors_combobox)
        self.layout.addLayout(self.sensors_layout)

        if(self.camera_layout.count() == 0):
            self.camera()
        
        self.layout.addLayout(self.sensors_layout)

    def clear_sensors(self):
        for i in range(self.sensors_layout.count()):
            if(self.sensors_layout.itemAt(i).layout() == None):
                self.sensors_layout.itemAt(i).widget().deleteLater()
        for i in range(self.camera_layout.count()):
            self.camera_layout.itemAt(i).widget().deleteLater()
        
        

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
clear.clicked.connect(w.clear_sensors)
w.show()
app.exec_()