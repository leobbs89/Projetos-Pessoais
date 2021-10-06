import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from GUI2 import Ui_MainWindow
from new_user_ui import Ui_New_user_window
import sys


class UserInterface(Ui_MainWindow):
    """Creates User interface"""

    def __init__(self, window, df):
        self.setupUi(window)
        self.df = df
        self.pushButton.clicked.connect(self.ok_button_pressed)
        self.new_user_button.clicked.connect(self.new_user_button_pressed)

    def ok_button_pressed(self):
        """Checks login and password"""
        password = self.password_line.text()
        id = self.id_line.text()
        if check_id(id, self.df):
            user = return_user(id, self.df)
            if user.check_password(password):
                show_popup("Message", "Password Correct")
            else:
                show_popup("Message", "Password incorrect")
        else:
            show_popup("Message", "User not found")

    def new_user_button_pressed(self):
        """Opens new user window"""
        self.window2 = QtWidgets.QMainWindow()
        self.ui = NewUserInterface(self.window2,self.df)
        self.window2.show()

class NewUserInterface(Ui_New_user_window):
    """Creates User interface"""

    def __init__(self,window, df):
        self.setupUi(window)
        self.df = df
        self.create_button.clicked.connect(self.button_pressed)

    def button_pressed(self):
        """Creates new user in dataframe"""
        password = self.password_line.text()
        id = self.user_line.text()
        name = 'Generic'
        new_user = User(name, id, password)
        df = insert_user(new_user, self.df)



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


def show_popup(title, text):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(text)

    x = msg.exec_()


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
    user_rows = df.where(df['ID'] == id)
    user_rows = user_rows.dropna()
    user_rows = user_rows.values.tolist()
    user = User(user_rows[0][1], user_rows[0][0], user_rows[0][2])
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
    main_window = QtWidgets.QMainWindow()
    ui = UserInterface(main_window, df)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
