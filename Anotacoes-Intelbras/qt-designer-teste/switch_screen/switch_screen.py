import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_switch_screen import Ui_StackedWidget

class SwitchScreen(QMainWindow, Ui_StackedWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.button_switch_screen.clicked.connect(self.switch_screen)
        self.stackedWidget.setCurrentIndex(0)
        
    def switch_screen(self):
        current_index = self.stackedWidget.currentIndex()
        if current_index == 0:
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.stackedWidget.setCurrentIndex(0)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SwitchScreen()
    window.show()
    sys.exit(app.exec())
