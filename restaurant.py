import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QGroupBox, QLabel
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Restaurant")
        vbox = QVBoxLayout()
        self.check_boxes()
        vbox.addWidget(self.groupbox)
        self.setLayout(vbox)
        self.label = QLabel("")
        vbox.addWidget(self.label)
        self.show()
    def check_boxes(self):
        self.groupbox = QGroupBox("What do you want to eat?")
        hbox = QHBoxLayout()

        self.check1 = QCheckBox("Pizza")
        self.check1.setChecked(False)
        self.check1.clicked.connect(self.checked)
        hbox.addWidget(self.check1)

        self.check2 = QCheckBox("Burritos")
        self.check2.setChecked(False)
        self.check2.clicked.connect(self.checked)
        hbox.addWidget(self.check2)

        self.check3 = QCheckBox("Hamburger")
        self.check1.setChecked(False)
        self.check3.clicked.connect(self.checked)
        hbox.addWidget(self.check3)

        self.groupbox.setLayout(hbox)
    def checked(self):
        price = 0
        if self.check1.isChecked():
            price = 0 + 10

        if self.check2.isChecked():
            price = 0 + 5

        if self.check3.isChecked():
            price = 0 + 5

        if self.check1.isChecked() and self.check2.isChecked():
            price = 0 + 15

        if self.check1.isChecked() and self.check3.isChecked():
            price = 0 + 15

        if self.check2.isChecked() and self.check3.isChecked():
            price = 0 + 10

        if self.check1.isChecked() and self.check2.isChecked() and self.check3.isChecked():
            price = 0 + 20

        self.label.setText("Total price is " + "$" + str(price))
app = QApplication(sys.argv)
window = Window()
app.exec_()