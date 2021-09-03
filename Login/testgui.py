from PyQt5 import QtCore, QtGui, QtWidgets
from GUI2 import Ui_MainWindow
import sys

class TestWindow(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.pushButton.clicked.connect(self.button_pressed)

    def button_pressed(self):
        password = self.password_line.text()
        id = self.id_line.text()
        print(f'Id = {id} password = {password}')

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = TestWindow(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
