from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.Pila_Stack import Stack

class DialogStock(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/Pila.ui", self)
        self.stack = Stack()
        
        self.btn_push.clicked.connect(self.push)
        self.btn_pop.clicked.connect(self.pop)
        self.btn_top.clicked.connect(self.top)
        self.btn_imprimir.clicked.connect(self.imprimir)
        
    def push(self):
        if self.txt_dato.text() == "":
            self.lbl_pila.setText("Ingrese un dato")
        else:
            self.stack.push(self.txt_dato.text())
            self.lbl_pila.setText("Se agregó el dato a la pila")
            self.txt_dato.setText("")
    
    def pop(self):
        self.lbl_pila.setText(self.stack.pop())
        self.txt_dato.setText("")
    
    def top(self):
        self.lbl_pila.setText(self.stack.top_of_stack())
        self.txt_dato.setText("")
    
    def imprimir(self):
        self.lbl_pila.setText(self.stack.print_stack())
        self.txt_dato.setText("")
        
        
    