from PyQt5 import QtCore, QtGui, QtWidgets

import sys


from LOGIN_GUI import Ui_Dialog

class TestWindow(Ui_Dialog):
    def __init__(self):
        super(TestWindow,self).__init__()
        self.pushButton.clicked.connect(self.pushButton.buttonpressed)

    def buttonpressed(self):
        password = self.Password_Line.text()
        id = self.ID_line.text()
        print(f'Id = {id} password = {password}')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())