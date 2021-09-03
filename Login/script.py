import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from GUI2 import Ui_MainWindow
import sys


class User_Interface(Ui_MainWindow):
    """Creates User interface"""

    def __init__(self, window, df):
        self.setupUi(window)
        self.df = df
        self.pushButton.clicked.connect(self.button_pressed)

    def button_pressed(self):
        """Checks login and password"""
        password = self.password_line.text()
        id = self.id_line.text()
        if check_id(id,self.df) :
            user = return_user(id,self.df)
            if user.check_password(password):
                self.show_poup("Message","Password Correct")
            else:
                self.show_poup("Message", "Password incorrect")
        else:
            self.show_poup("Message","User not found")

    def show_poup(self,title,text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)

        x = msg.exec_()

class User:
    """Maintain user information"""

    def __init__(self, name: str, id: str, password: str):
        self.name = name
        self.id = id
        self.password = password

    def check_password(self, password: str) -> bool:
        if self.password == password:
            return True
        else:
            return False


# Insert user in DataFrame
def insert_user(user: User, df: pd.DataFrame) -> pd.DataFrame:
    df = df.append({"NAME": user.name, "ID": user.id, "PASSWORD": user.password}, ignore_index=True, sort=True)
    df = df.sort_values("NAME")
    return df


# Checks if ID is in DataFrame
def check_id(id: str, df: pd.DataFrame) -> bool:
    if id in df["ID"].tolist():
        return True
    else:
        return False


# Return user from DataFrame
def return_user(id: str, df: pd.DataFrame) -> User:
    user_rown = df.where(df['ID'] == id)
    user_rown = user_rown.dropna()
    user_rown = user_rown.values.tolist()
    user = User(user_rown[0][1], user_rown[0][0], user_rown[0][2])
    return user


# MAIN FUNCTION
def main():
    # Create DataFrame
    df = pd.DataFrame(columns=["NAME", "ID", "PASSWORD"])
    user1 = User("Leandro", "leobbs89", "ima450")
    user2 = User("Carolina", "camposka88", "carol1812")
    df = insert_user(user1, df)
    df = insert_user(user2, df)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = User_Interface(MainWindow,df)
    MainWindow.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()
