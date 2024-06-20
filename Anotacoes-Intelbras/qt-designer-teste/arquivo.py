import sys
from mainwindow_screen.ui_arquivo import Ui_MainWindow
from password_screen.password_screen import PasswordScreen
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
from PySide6.QtCore import Slot

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # Aqui você pode conectar os sinais dos botões aos slots (funções) desejados
        self.button_model_a.clicked.connect(self.show_password_screen)
        self.button_model_b.clicked.connect(self.show_password_screen)
        self.button_model_c.clicked.connect(self.show_password_screen)
        self.button_model_d.clicked.connect(self.show_password_screen)
        self.button_model_e.clicked.connect(self.show_password_screen)
        self.button_model_f.clicked.connect(self.show_password_screen)
        ##self.button_change_tolerance.clicked.connect(self.show_password_screen)

    def show_password_screen(self):
        self.password_screen = PasswordScreen()
        self.password_screen.show()
        ## comando para fechar a mainwindow quando abrir a secundary window
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())       