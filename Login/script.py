class User():
    """Mantain user information"""

    def __init__(self, name, id, password):
        self.name = name
        self.id = id
        self.password = password

    def check_password(self,password):
        if self.password == password :
            return True
        else:
            return False

#Insert user in DataFrame
def insert_user(user,df):
    df = df.append({"NAME":user.name,"ID":user.id,"PASSWORD":user.password},ignore_index=True,sort=True)
    df = df.sort_values("NAME")
    return df

#Checks if ID is in DataFrame
def check_id(id,df):
    if id in df["ID"].tolist() :
        return True
    else:
        return False

#Return user from DataFrame
def return_user(id,df):
    user_rown = df.loc[df.index[df["ID"] == "camposka88"]]
    user = User(user_rown["NAME"],user_rown["ID"],user_rown["PASSWORD"])
    return user

#Create DataFrame
import pandas as pd
df = pd.DataFrame(columns = ["NAME","ID","PASSWORD"])
user1 = User("Leandro","leobbs89","ima450")
user2 = User("Carolina","camposka88","carol1812")
df = insert_user(user1,df)
df = insert_user(user2,df)
print(df)
#Create Interface
from PyQt5 import QtCore, QtGui, QtWidgets, QMessageBox
from qgis.PyQt.QtWidgets import QMessageBox


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(186, 164)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 10, 151, 141))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Password_Line = QtWidgets.QLineEdit(self.widget)
        self.Password_Line.setObjectName("Password_Line")
        self.verticalLayout.addWidget(self.Password_Line)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.ID_line = QtWidgets.QLineEdit(self.widget)
        self.ID_line.setObjectName("ID_line")
        self.verticalLayout.addWidget(self.ID_line)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.clicked)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LOGIN"))
        self.label.setText(_translate("Dialog", "LOGIN :"))
        self.label_2.setText(_translate("Dialog", "PASSWORD"))
        self.pushButton.setText(_translate("Dialog", "OK"))

    def clicked(self):
        if check_id(self.ID_line.text(),df) :
            user = return_user(self.ID_line,df)
            if user.check_password(self.Password_Line.text()) :
                msg = QMessageBox()
                msg.setWindowTitle("!!!")
                msg.setText("Password correct")
                x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("User not found")
            x = msg.exec_()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
