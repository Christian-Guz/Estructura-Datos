from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from load.load_listas_enlazadas import DialogListasEnlazadas

class LoadMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/menu.ui", self)
        
        self.actionListas_Enlazadas.triggered.connect(self.load_listas_enlazadas)
        self.actionSalir.triggered.connect(self.close)
        
    def load_listas_enlazadas(self):
        listas_enlazadas = DialogListasEnlazadas()
        listas_enlazadas.exec_()
    
    def close(self):
        return super().close()
