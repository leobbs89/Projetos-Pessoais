import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from GUI2 import Ui_MainWindow
from new_user_ui import Ui_New_user_window
import sys


class UserInterface(Ui_MainWindow):
    """Creates User interface"""

    def __init__(self, window):
        self.setupUi(window)
        self.pushButton.clicked.connect(self.ok_button_pressed)
        self.new_user_button.clicked.connect(self.new_user_button_pressed)

    def ok_button_pressed(self):
        """Checks login and password"""
        password = self.password_line.text()
        id = self.id_line.text()
        if check_id(id):
            user = return_user(id)
            if user.check_password(password):
                show_popup("Message", "Password Correct")
            else:
                show_popup("Message", "Password incorrect")
        else:
            show_popup("Message", "User not found")

    def new_user_button_pressed(self):
        """Opens new user window"""
        self.window2 = QtWidgets.QMainWindow()
        self.ui = NewUserInterface(self.window2)
        self.window2.show()


class NewUserInterface(Ui_New_user_window):
    """Creates User interface"""

    def __init__(self, window):
        self.setupUi(window)
        self.create_button.clicked.connect(self.button_pressed)

    def button_pressed(self):
        """Creates new user in dataframe"""
        password = self.password_line.text()
        id = self.user_line.text()
        name = self.name_line.text()
        new_user = User(name, id, password)
        insert_user(new_user)


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
def insert_user(user: User):
    df = open_dataframe()
    df = df.append({"NAME": user.name, "ID": user.id, "PASSWORD": user.password}, ignore_index=True, sort=True)
    df = df.sort_values("NAME")
    save_dataframe(df)


# Checks if ID is in DataFrame
def check_id(id: str) -> bool:
    df = open_dataframe()
    if id in df["ID"].tolist():
        return True
    else:
        return False


# Return user from DataFrame
def return_user(id: str) -> User:
    df = open_dataframe()
    user_rows = df.where(df['ID'] == id)
    user_rows = user_rows.dropna()
    user_rows = user_rows.values.tolist()
    user = User(user_rows[0][1], user_rows[0][0], user_rows[0][2])
    return user


def open_dataframe():
    df = pd.read_csv('database.csv')
    return df


def save_dataframe(df):
    df.to_csv('database.csv', index=False)


# MAIN FUNCTION
def main():
    # Create DataFrame
    df = pd.DataFrame(columns=["NAME", "ID", "PASSWORD"])
    save_dataframe(df)
    #Runs main window
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UserInterface(main_window)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
