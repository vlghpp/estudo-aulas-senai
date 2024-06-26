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
        # Executa uma função lambda(anônima) em linha, fazendo com que chame a função de mostrar a tela passando o modelo
        self.button_model_a.clicked.connect(lambda: self.set_model_switch('model_a'))
        self.button_model_b.clicked.connect(lambda: self.set_model_switch('model_b'))
        self.button_model_c.clicked.connect(lambda: self.set_model_switch('model_c'))
        self.button_model_d.clicked.connect(lambda: self.set_model_switch('model_d'))
        self.button_model_e.clicked.connect(lambda: self.set_model_switch('model_e'))
        self.button_model_f.clicked.connect(lambda: self.set_model_switch('model_f'))

    def set_model_switch(self, model_name):
        if model_name == 'model_a':
            """
            Aqui ficaria responsável pela conexão com o arduino, mandando o sinal de qual dos modelos de switch foi escolhido.
            por exemplo: print("O modelo A foi escolhido!")

            E logo abaixo daria continuação ao código, executando segunda tela com o video
            """
            self.show_secondary_screen()


    def show_secondary_screen(self):
        self.password_screen = PasswordScreen()
        self.password_screen.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())       