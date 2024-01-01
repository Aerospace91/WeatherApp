from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('Weather.ui', self)
        self.show()

app = QApplication([])
window = Ui()
app.exec()