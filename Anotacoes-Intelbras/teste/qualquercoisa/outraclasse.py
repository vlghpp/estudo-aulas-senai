from ui_main import Ui_MainWindow
class OutraTeste:
    def __init__(self,ui) -> None:
        self.ui:Ui_MainWindow = ui

        self.ui.pushButton.clicked.connect(self.minhafuncao)


    def minhafuncao(self):
        ...