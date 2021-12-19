import PyQt5.QtWidgets as pyqt
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
import sys


class MainWindow(pyqt.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configurations")
        self.setGeometry(400, 400, 700, 400)

        # Horizontal layout for the label number of sensors and textbox
        self.horizontal_layout = pyqt.QHBoxLayout()

        # Parent layout for any layout in the class
        self.layout = pyqt.QVBoxLayout()

        # Adding the horizontal_layout to the parent layout
        self.layout.addLayout(self.horizontal_layout)

        # Setting the parent layout as the main layout
        container = pyqt.QWidget()
        container.setLayout(self.layout)
        self.setMenuWidget(container)

        # Open in full screen
        self.showMaximized()

    def label(self, text):
        label = pyqt.QLabel (text, self)
        label.setFont(QtGui.QFont('Arial', 15)) 
        label.adjustSize()
        self.horizontal_layout.addWidget(label)

    def textBox(self):
        self.textbox = pyqt.QLineEdit(self)
        self.horizontal_layout.addWidget(self.textbox)

    def button(self):
        self.pb = pyqt.QPushButton()
        self.pb.setText("Enter")
        self.horizontal_layout.addWidget(self.pb)

    def button_click(self):
        number_of_sensors = self.textbox.text
        print (number_of_sensors)

app = pyqt.QApplication(sys.argv)
w = MainWindow()
w.label("Number of sensors")
w.textBox()
w.show()
app.exec_()