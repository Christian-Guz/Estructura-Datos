from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from load.load_listas_enlazadas import DialogListasEnlazadas
from load.load_pila_stack import DialogStock
from load.load_aplicacion import DialogAplicacion

class LoadMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/menu.ui", self)
        
        self.actionListas_Enlazadas.triggered.connect(self.load_listas_enlazadas)
        self.actionPila_o_Stack.triggered.connect(self.loadPila_Stack)
        self.actionAplicacion.triggered.connect(self.loadAplicacion)
        self.actionSalir.triggered.connect(self.close)
        
    def load_listas_enlazadas(self):
        listas_enlazadas = DialogListasEnlazadas()
        listas_enlazadas.exec_()
    
    def loadPila_Stack(self):
        pila_stack = DialogStock()
        pila_stack.exec_()
    
    def loadAplicacion(self):
        aplicacion = DialogAplicacion()
        aplicacion.exec_()
    
    def close(self):
        return super().close()
