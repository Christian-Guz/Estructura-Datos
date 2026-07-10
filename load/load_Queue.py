from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.Cola_Queue import Queue

class DialogQueue(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/Cola_Queue.ui", self)
        self.queue = Queue()
        
        self.btn_ingresar.clicked.connect(self.ingresar)
        self.btn_eliminar.clicked.connect(self.eliminar)
        self.btn_primer.clicked.connect(self.impr_primer)
        self.btn_ultimo.clicked.connect(self.impr_ultimo)
        self.btn_fila.clicked.connect(self.imprimir)
        self.btn_vacio.clicked.connect(self.list_vacio)
        
    def ingresar(self):
        if self.txt_dato.text() == "":
            self.lbl_lista.setText("Ingrese un dato")
        else:
            self.lbl_lista.setText(self.queue.enQueue(self.txt_dato.text()))
            self.txt_dato.setText("")
    
    def eliminar(self):
        self.lbl_lista.setText(self.queue.deQueue())
        self.txt_dato.setText("")
    
    def impr_primer(self):
        self.lbl_lista.setText(self.queue.firstQueue())
        self.txt_dato.setText("")
    
    def impr_ultimo(self):
        self.lbl_lista.setText(self.queue.lastQueue())
        self.txt_dato.setText("")
    
    def imprimir(self):
        self.lbl_lista.setText(self.queue.printQueue())
        self.txt_dato.setText("")
        
    def list_vacio(self):
        self.lbl_lista.setText(str(self.queue.isEmpty()))
        self.txt_dato.setText("")
    