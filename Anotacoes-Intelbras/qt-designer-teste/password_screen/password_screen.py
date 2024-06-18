from password_screen.ui_password_screen import Ui_PasswordScreen
from PySide6.QtWidgets import QDialog


class PasswordScreen(QDialog, Ui_PasswordScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
