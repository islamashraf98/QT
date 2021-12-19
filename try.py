import sys
from PyQt5.QtWidgets import QVBoxLayout, QComboBox, QApplication, QWidget, QLabel

class Window():
    app = QApplication(sys.argv)
    widget = QWidget()
    textlabel = QLabel(widget)
    combobox = QComboBox()
    combobox.addItem('one')
    combobox.addItem('two')
    layout = QVBoxLayout()
    layout.addWidget(combobox)
    widget.setGeometry(400, 400, 400, 200)
    widget.setWindowTitle("First PyQt5")
    widget.setLayout(layout)
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()